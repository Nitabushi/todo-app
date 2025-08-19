from datetime import datetime
from . import db

class Todo(db.Model):
    __tablename__ = "todos"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    detail = db.Column(db.Text, nullable=True)
    status = db.Column(db.Integer, default=0)  # 0=未完, 1=完了
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
