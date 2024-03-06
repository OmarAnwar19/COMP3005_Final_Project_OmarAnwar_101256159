import re

def validate_password(password):
    if len(password) < 6:
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search("[A-Z]", password):
        return False
    return True


def format_date(date):
    return date.strftime("%B %d, %Y, %I:%M %p %Z")