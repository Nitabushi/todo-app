import re

class PasswordValidationError(ValueError):
    pass

def validate_password(plain_password: str) -> None:
    """
    8〜16文字・大文字/小文字/数字/記号を各1つ以上含むことを要求。
    条件を満たさない場合は PasswordValidationError を送出。
    """
    if not isinstance(plain_password, str):
        raise PasswordValidationError("パスワードは文字列で指定してください")

    if not (8 <= len(plain_password) <= 16):
        raise PasswordValidationError("パスワードは8〜16文字にしてください")
    if not re.search(r"[A-Z]", plain_password):
        raise PasswordValidationError("大文字を1つ以上含めてください")
    if not re.search(r"[a-z]", plain_password):
        raise PasswordValidationError("小文字を1つ以上含めてください")
    if not re.search(r"[0-9]", plain_password):
        raise PasswordValidationError("数字を1つ以上含めてください")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", plain_password):
        raise PasswordValidationError("特殊記号を1つ以上含めてください")
