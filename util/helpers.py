import re

def validate_password(password):
    if len(password) < 6:
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search("[A-Z]", password):
        return False
    return True


def format_datetime(date):
    return date.strftime("%B %d, %Y, %I:%M %p %Z")


def format_date(date):
    return date.strftime("%Y-%m-%d")


def format_datetime_for_html(datetime_obj):
    return datetime_obj.strftime("%Y-%m-%dT%H:%M")