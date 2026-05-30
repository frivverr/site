import os
from flask import Flask, render_template

app = Flask(__name__)

# Настройки по умолчанию для страницы
SITE_CONFIG = {
    "title": "DEADPRACTICE SITE",
    "name": "DEADPRACTICE SITE",
    "headline": "@takuxkakya<- Ты ответил: Ой, я так не могу! Я просто обычный парень, который просто и беззадачно жмет свой телефон🤷‍♂️.",
    "description": "🐭🐭🐭🐭",
    "panels": [
        {"title": "тгк", "text": "https://t.me/Deadpractice\nhttps://t.me/heppylikeslon"},
        {"title": "тик ток", "text": "https://www.tiktok.com/@0.3breakfour?_r=1&_t=ZS-96ncw3zPTQi"},
        {"title": "Обо мне", "text": " оборотень!"}
    ],
    "profile_image": "profile-placeholder.png",
    "background_image": "background-placeholder.jpg",
}

@app.route('/')
def index():
    return render_template('index.html', config=SITE_CONFIG)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)
