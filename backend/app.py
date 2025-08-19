# backend/app.py
from flask import Flask, jsonify
from flask_cors import CORS

from .config import Config
from .models import db  # User/Todo は __init__ で読み込まれる

def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)

    # CORS（必要に応じて origins を限定）
    CORS(app)

    # SQLAlchemy 初期化
    db.init_app(app)

    @app.get("/health")
    def health():
        return jsonify({"status": "ok"})

    # 学習用：最初のテーブル作成（本番は Flask-Migrate 推奨）
    @app.post("/init-db")
    def init_db():
        with app.app_context():
            db.create_all()
        return jsonify({"message": "created tables"}), 201

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="127.0.0.1", port=5000, debug=True)
