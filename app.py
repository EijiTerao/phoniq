# PhonIQ - 発音記号特化型英単語学習アプリ
# メインエントリポイント

from flask import Flask
from routes.theory import theory_bp
from routes.practice import practice_bp
from routes.api import api_bp

app = Flask(__name__)
app.secret_key = 'phoniq-secret-key-change-in-production'

# ブループリント登録
app.register_blueprint(theory_bp, url_prefix='/theory')
app.register_blueprint(practice_bp, url_prefix='/practice')
app.register_blueprint(api_bp, url_prefix='/api')

@app.route('/')
def index():
    from flask import render_template
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
