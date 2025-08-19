import importlib

def test_public_api_of_validator():
    v = importlib.import_module("backend.validators")

    # __all__ に公開APIが明示されていること
    assert set(v.__all__) == {"validate_password", "PasswordValidationError"}

    # 公開APIとしてアクセスできること
    assert hasattr(v, "validate_password")
    assert hasattr(v, "PasswordValidationError")

    # 「password という内部モジュール名」に直接依存しなくていいことの確認
    # ⇒ つまり backend.validators だけで必要なものが揃う
    validate_password = getattr(v, "validate_password")
    PasswordValidationError = getattr(v, "PasswordValidationError")
    assert callable(validate_password)
    assert isinstance(PasswordValidationError, type)