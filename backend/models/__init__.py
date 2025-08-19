from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# 個別モデルを遅延インポート（循環参照を避けるため）
from .user import User  # noqa: E402,F401
from .todo import Todo  # noqa: E402,F401

__all__ = ["db", "User", "Todo"]
