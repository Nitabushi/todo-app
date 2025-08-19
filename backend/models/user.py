# backend/models/user.py
from datetime import datetime
from sqlalchemy.orm import validates
from . import db
from backend.validators import validate_password, PasswordValidationError

# 役割の定数（拡張しやすい）
ROLE_USER = "user"
ROLE_ADMIN = "admin"
ALLOWED_ROLES = (ROLE_USER, ROLE_ADMIN)

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False, index=True)
    # 平文は入れない。必ずハッシュを入れる
    password_hash = db.Column(db.String(255), nullable=False)

    # 文字列で持つ（MySQLのCHECK制約は8.0.16+で有効だが、アプリ側でも検証する）
    role = db.Column(db.String(20), nullable=False, default=ROLE_USER)

    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    # User 1:N Todo
    todos = db.relationship(
        "Todo",
        backref="user",
        cascade="all, delete-orphan"
    )

    # パスワードのヘルパー
    def set_password(self, plain_password: str):
        """
        バリデーションは validator に委譲し、OKならハッシュ化して保存。
        """
        from werkzeug.security import generate_password_hash

        # ここで学習向けに明示のバリデーション。NGなら例外を送出。
        validate_password(plain_password)
        self.password_hash = generate_password_hash(plain_password)

    def check_password(self, plain_password: str) -> bool:
        from werkzeug.security import check_password_hash
        return check_password_hash(self.password_hash, plain_password)

    def is_admin(self) -> bool:
        return self.role == ROLE_ADMIN

    @validates("role")
    def validate_role(self, key, value: str):
        """
        DBのCHECK制約だけに頼らず、アプリ側でも厳格に検証。
        """
        if value not in ALLOWED_ROLES:
            raise ValueError(f"role は {ALLOWED_ROLES} のいずれかにしてください")
        return value
