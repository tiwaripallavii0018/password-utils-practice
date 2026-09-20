import re

def is_strong_password(password):
    """Password must contain at least 8 characters,
    one uppercase letter and one digit."""

    if not isinstance(password, str):
        raise TypeError("password must be a string")

    if len(password) < 8:
        return False

    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)

    return has_upper and has_digit


def mask_password(password):
    """Return password with only first and last character visible."""

    if not is_strong_password(password):
        raise ValueError("Weak password")

    return password[0] + "*"*(len(password)-2) + password[-1]


def contains_special(password):
    """Return True if password contains a special character."""

    special = r"[!@#$%^&*()]"

    return re.search(special,password) is not None