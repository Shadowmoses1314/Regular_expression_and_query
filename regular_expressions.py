import re


def validate_email(email):
    if email is None:
        return False
    pattern = r'^[\w\.-]{1,100}@[\w\.-]{1,255}\.[\w]{1,63}$'
    if re.match(pattern, email):
        return True
    return False


def find_words_starting_with_s(string):
    pattern = r'\b[sS]\w+'
    matches = re.findall(pattern, string)
    return matches


def find_numbers(string):
    pattern = r'\b\d+\b'
    matches = re.findall(pattern, string)
    return matches


def check_agreement(string):
    pattern = r'^Да(?!,\s*нет)'
    match = re.search(pattern, string)
    return bool(match)


def find_dates(string):
    pattern = r'\b\d{2}/\d{2}/\d{4}\b'
    matches = re.findall(pattern, string)
    return matches
