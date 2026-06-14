# PhonIQ - Phase 1 ルーティング

from flask import Blueprint, render_template
from data.theory import SPELLING_CATEGORIES, IPA_SYMBOLS

theory_bp = Blueprint('theory', __name__)

@theory_bp.route('/')
def theory_home():
    """Phase 1 トップ: 2つの学習層を選ぶ画面"""
    return render_template('theory/index.html',
                           spelling_categories=SPELLING_CATEGORIES,
                           ipa_symbols=IPA_SYMBOLS)

@theory_bp.route('/spelling')
def spelling_home():
    """Layer A: 文字のつながりから学ぶ - カテゴリ一覧"""
    return render_template('theory/spelling_home.html',
                           categories=SPELLING_CATEGORIES)

@theory_bp.route('/spelling/<category_id>')
def spelling_detail(category_id):
    """Layer A: 個別カテゴリの詳細ページ"""
    category = next((c for c in SPELLING_CATEGORIES if c['id'] == category_id), None)
    if not category:
        return render_template('404.html'), 404
    return render_template('theory/spelling_detail.html', category=category)

@theory_bp.route('/ipa')
def ipa_home():
    """Layer B: 発音記号から学ぶ - IPA 解説"""
    return render_template('theory/ipa_home.html', ipa_data=IPA_SYMBOLS)

@theory_bp.route('/ipa/<symbol_category_id>')
def ipa_detail(symbol_category_id):
    """Layer B: IPA カテゴリ詳細"""
    cat = next((c for c in IPA_SYMBOLS['categories'] if c['id'] == symbol_category_id), None)
    if not cat:
        return render_template('404.html'), 404
    return render_template('theory/ipa_detail.html', category=cat, ipa_data=IPA_SYMBOLS)
