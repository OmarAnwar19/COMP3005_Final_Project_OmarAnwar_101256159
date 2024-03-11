import re

# this function checks if a given password is valid
def validate_password(password):
    # password must be at least 6 characters long, and contain a number and an uppercase letter
    if len(password) < 6:
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search("[A-Z]", password):
        return False
    return True


# helper function to format datetime objects
def format_datetime(date):
    return date.strftime("%B %d, %Y, %I:%M %p %Z")


# helper function to format date objects
def format_date(date):
    return date.strftime("%Y-%m-%d")


# helper function to format datetime objects for HTML input fields
def format_datetime_for_html(datetime_obj):
    return datetime_obj.strftime("%Y-%m-%dT%H:%M")