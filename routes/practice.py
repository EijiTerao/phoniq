# PhonIQ - Phase 2 ルーティング

from flask import Blueprint, render_template, request, jsonify, session
from data.words import WORDS
from utils.question_generator import generate_question_set

practice_bp = Blueprint('practice', __name__)

@practice_bp.route('/')
def practice_home():
    """Phase 2 トップ: 問題フェーズのホーム"""
    return render_template('practice/index.html')

@practice_bp.route('/quiz')
def quiz():
    """問題ページ: クエリパラメータで単語を指定可能"""
    word_filter = request.args.get('category', None)  # カテゴリフィルタ
    target_word = request.args.get('word', None)       # 特定単語（理論ページからのリンク用）
    return render_template('practice/quiz.html',
                           word_filter=word_filter,
                           target_word=target_word)

@practice_bp.route('/result')
def result():
    """結果ページ"""
    return render_template('practice/result.html')
