import pytest

from src.password_utils import (
    is_strong_password,
    mask_password,
    contains_special
)


def test_password_valid():

    password="Password1"

    assert is_strong_password(password)==True


def test_password_type():

    with pytest.raises(TypeError):
        is_strong_password(1234)


# def test_mask_password():
#
#     password="Password1"
#
#     assert mask_password(password)=="P*******1"