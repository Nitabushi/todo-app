import pytest
from backend.validators import validate_password, PasswordValidationError

# 通るべきパスワード（境界値含む）
@pytest.mark.parametrize("pw", [
    "Aa1!aaaa",      # 8文字(最小)
    "Aa1!aaaaBBBB",  # 中間
    "A1!aaaaabbbbCC",# 14文字
    "Aa1!aaaaBBBBCC",# 16文字(最大)
])
def test_validate_password_ok(pw):
    # 例外が出なければ合格
    validate_password(pw)

# 型・長さの境界、各要素欠落を網羅
@pytest.mark.parametrize("pw, msg_fragment", [
    (12345, "文字列で指定"),                # 非文字列
    ("Aa1!aaa", "8〜16文字"),              # 7文字（最小未満）
    ("Aa1!aaaaBBBBCCDDD", "8〜16文字"),     # 17文字（最大超過）
    ("aa1!aaaa", "大文字"),                 # 大文字不足
    ("AA1!AAAA", "小文字"),                 # 小文字不足
    ("Aa!aaaaa", "数字"),                   # 数字不足
    ("Aa1aaaaa", "特殊記号"),               # 記号不足
])
def test_validate_password_ng(pw, msg_fragment):
    with pytest.raises(PasswordValidationError) as e:
        validate_password(pw)
    assert msg_fragment in str(e.value)

def test_error_type_is_subclass_of_valueerror():
    assert issubclass(PasswordValidationError, ValueError)
