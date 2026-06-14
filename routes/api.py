# PhonIQ - API エンドポイント
# フロントエンド（JS）から呼ばれるJSON API

from flask import Blueprint, jsonify, request
from data.words import WORDS
from utils.question_generator import generate_question_set, validate_question_set

api_bp = Blueprint('api', __name__)

@api_bp.route('/question')
def get_question():
    """
    問題セットを返す API
    クエリパラメータ:
        word: 特定の単語を指定（任意）
        category: カテゴリフィルタ（任意）
        gender: 音声の性別 'male' or 'female'（任意）
    """
    word_query = request.args.get('word', None)
    category   = request.args.get('category', None)
    gender     = request.args.get('gender', 'female')  # デフォルト female

    # 単語を絞り込む
    pool = WORDS
    if word_query:
        pool = [w for w in WORDS if w['word'].lower() == word_query.lower()]
    elif category:
        pool = [w for w in WORDS if w['category'] == category]

    if not pool:
        return jsonify({"error": "No words found"}), 404

    import random
    target = random.choice(pool)

    # 問題セット生成（バリデーション込み）
    question_set = generate_question_set(target, WORDS)
    if question_set is None:
        return jsonify({"error": "Could not generate valid question"}), 500

    # 音声URLを付加（Web Speech API 用のテキストを返す）
    question_set['audio'] = {
        "text": target['word'],
        "gender": gender  # クライアント側で Web Speech API に渡す
    }

    return jsonify(question_set)


@api_bp.route('/words')
def get_words():
    """単語一覧 API（カテゴリフィルタ対応）"""
    category = request.args.get('category', None)
    if category:
        result = [w for w in WORDS if w['category'] == category]
    else:
        result = WORDS
    return jsonify(result)


@api_bp.route('/categories')
def get_categories():
    """利用可能なカテゴリ一覧"""
    cats = list(set(w['category'] for w in WORDS))
    return jsonify(sorted(cats))
