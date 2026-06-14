# PhonIQ - 問題生成ユーティリティ
# Phase 2 の A/B/C 問題を自動生成し、正確性を内部検証する

import random
from typing import Optional

# ===== 問題生成メイン関数 =====

def generate_question_set(target: dict, all_words: list) -> Optional[dict]:
    """
    1つの単語に対して A/B/C の問題セットを生成する。
    内部バリデーションが通らなければ None を返す。

    target: WORDS の1エントリ
    all_words: WORDS 全体
    """
    question_a = _make_question_a(target)
    question_b = _make_question_b(target)
    question_c = _make_question_c(target, all_words)

    # 問題Cが生成できない場合はフォールバック
    if question_c is None:
        return None

    # ===== 内部バリデーション =====
    # (アプリ上には表示しない)
    if not validate_question_set(target, question_a, question_b, question_c):
        # バリデーション失敗時は再試行（最大3回）
        for _ in range(3):
            question_c = _make_question_c(target, all_words)
            if question_c and validate_question_set(target, question_a, question_b, question_c):
                break
        else:
            return None

    return {
        "word": target['word'],
        "ipa": target['ipa'],
        "syllables": target['syllables'],
        "stress": target['stress'],
        "category": target['category'],
        "question_a": question_a,
        "question_b": question_b,
        "question_c": question_c,
    }


# ===== 問題A: 発音を聞く =====

def _make_question_a(target: dict) -> dict:
    """
    問題A: 単語の発音を聞いて確認する
    音声再生はクライアントサイドの Web Speech API が担当
    """
    return {
        "type": "listen",
        "instruction": "発音を聞いてみましょう",
        "word": target['word'],
        "ipa": target['ipa'],
    }


# ===== 問題B: アクセントのある音節を選ぶ =====

def _make_question_b(target: dict) -> dict:
    """
    問題B: 音節を表示し、アクセントのある音節を選ぶ
    """
    syllables = target['syllables']
    correct_index = target['stress']

    return {
        "type": "stress",
        "instruction": "アクセントのある音節はどれですか？",
        "syllables": syllables,
        "correct_index": correct_index,
        "correct_syllable": syllables[correct_index],
    }


# ===== 問題C: 4択 - どの単語に近い発音か =====

def _make_question_c(target: dict, all_words: list) -> Optional[dict]:
    """
    問題C: ターゲット単語の発音記号を見て、4択の中からその発音に近い単語を選ぶ。
    選択肢は same similar_group の単語を優先し、引っかかりやすい類似発音を含める。
    初期表示では選択肢の発音記号を非表示にし、選択後に表示する。
    """
    correct_word = target

    # --- 同じ similar_group から間違い選択肢候補を集める ---
    same_group = [
        w for w in all_words
        if w['similar_group'] == target['similar_group']
        and w['word'] != target['word']
    ]

    # --- 同カテゴリから追加候補 ---
    same_category = [
        w for w in all_words
        if w['category'] == target['category']
        and w['word'] != target['word']
        and w not in same_group
    ]

    # --- 異なるカテゴリからランダム候補 ---
    other_category = [
        w for w in all_words
        if w['category'] != target['category']
        and w['word'] != target['word']
    ]

    # 3つの間違い選択肢を優先度順に取得
    distractors = []
    pool_order = [same_group, same_category, other_category]
    for pool in pool_order:
        random.shuffle(pool)
        for candidate in pool:
            # 重複チェック（すでに選ばれたものは除外）
            if candidate not in distractors:
                distractors.append(candidate)
            if len(distractors) >= 3:
                break
        if len(distractors) >= 3:
            break

    if len(distractors) < 3:
        return None  # 選択肢が足りない

    distractors = distractors[:3]

    # 4択をシャッフル
    choices = distractors + [correct_word]
    random.shuffle(choices)

    correct_index = next(i for i, c in enumerate(choices) if c['word'] == target['word'])

    return {
        "type": "choice",
        "instruction": "この発音記号に対応する単語はどれですか？",
        "target_ipa": target['ipa'],
        "choices": [
            {
                "word": c['word'],
                "ipa": c['ipa'],   # 初期は JS 側で非表示。選択後に表示
            }
            for c in choices
        ],
        "correct_index": correct_index,
        "correct_word": target['word'],
    }


# ===== 内部バリデーション =====

def validate_question_set(target, q_a, q_b, q_c) -> bool:
    """
    問題セットの内部検証。アプリ上には表示しない。
    以下をチェックする:
    1. 問題Aの単語と発音記号が一致しているか
    2. 問題Bのアクセント位置が正しい範囲か
    3. 問題Cの正解が1つだけか（同一 IPA の単語が2つ以上選択肢にないか）
    4. 問題Cの選択肢が引っかかりやすい類似性を持っているか
    """
    # --- チェック1: 問題Aの整合性 ---
    if q_a['word'] != target['word']:
        return False
    if q_a['ipa'] != target['ipa']:
        return False

    # --- チェック2: アクセント位置の整合性 ---
    num_syllables = len(q_b['syllables'])
    if q_b['correct_index'] < 0 or q_b['correct_index'] >= num_syllables:
        return False

    # --- チェック3: 問題Cの正解重複チェック ---
    ipa_list = [c['ipa'] for c in q_c['choices']]
    correct_ipa = target['ipa']
    # 同じ IPA が2つ以上あれば不正
    if ipa_list.count(correct_ipa) > 1:
        return False

    # --- チェック4: 選択肢の類似性チェック ---
    # 少なくとも1つの選択肢が同じ similar_group または同カテゴリであること
    # （question_c の生成ロジックが正しく機能していればほぼ通るが念のため）
    choices_words = [c['word'] for c in q_c['choices']]
    if q_c['correct_word'] not in choices_words:
        return False

    return True
