import pytest
from regular_expressions import (validate_email,
                                 find_words_starting_with_s,
                                 find_numbers,
                                 check_agreement,
                                 find_dates
                                 )


@pytest.mark.parametrize(
    "email, expected_result",
    [
        ("test@example.com", True),
        ("user.name@example.co.uk", True),
        ("firstname.lastname1234@example-domain.com", True),
        ("invalid_email", False),
        ("user@example", False),
        ("user@example.", False),
        ("user@.com", False),
        ("", False),
        (None, False),
        ("user_123@example.com", True),
        ("user-name@example.com", True),
        ("user+name@example.com", False),
        ("TEST@EXAMPLE.COM", True),
        ("  test@example.com  ", False),
        ("пользователь@пример.рф", True),
        ("a" * 100 + "@example.com", True),
        ("test@" + "a" * 255 + ".com", True),
        ("test@" + "a" * 256 + ".com", False),
        ("test@example." + "a" * 63, True),
        ("test@example." + "a" * 64, False),
    ],
)
def test_validate_email(email, expected_result):
    assert validate_email(email) is expected_result


@pytest.mark.parametrize(
    "string, expected_result",
    [
        ("She sells seashells by the seashore.", ['She',
                                                  'sells',
                                                  'seashells', 'seashore']),
        ("Sun is shining and the sky is blue.", ['Sun', 'shining', 'sky']),
        ("The quick brown fox jumps over the lazy dog.", []),
        ("Singing in the rain.", ['Singing']),
        ("sailing on the sea", ['sailing', 'sea']),
        ("She saw a shooting star.", ['She', 'saw', 'shooting', 'star']),
        ("secrets and surprises", ['secrets', 'surprises']),
    ],
)
def test_find_words_starting_with_s(string, expected_result):
    assert find_words_starting_with_s(string) == expected_result


@pytest.mark.parametrize(
    "string, expected_result",
    [
        ("There are 10 cats.", ['10']),
        ("The answer is 42.", ['42']),
        ("The temperature is -5 degrees Celsius.", ['5']),
        ("The price is $99.99.", ['99', '99']),
        ("The population of the city is 1234567.", ['1234567']),
        ("The year is 2023.", ['2023']),
        ("No numbers in this string.", []),
        ("12345", ['12345']),
        ("123a45", []),
        ("Test 123 Test 456", ['123', '456']),
    ],
)
def test_find_numbers(string, expected_result):
    assert find_numbers(string) == expected_result


@pytest.mark.parametrize(
    "string, expected_result",
    [
        ("Да, интересно", True),
        ("Да, согласен", True),
        ("Да, давайте", True),
        ("Да, нет, не интересно", False),
        ("Да, нет, не хочу", False),
        ("Да, может быть", True),
        ("Да, но только если", True),
        ("Да, иначе", True),
        ("Да, необходимо", True),
        ("Да", True),
        ("Нет, интересно", False),
        ("Да, нет", False),
        ("Да, может и нет", True),
    ],
)
def test_check_agreement(string, expected_result):
    assert check_agreement(string) == expected_result


@pytest.mark.parametrize(
    "string, expected_result",
    [
        ("Today is 01/07/2023.", ["01/07/2023"]),
        ("The event will take place on 15/12/2022.", ["15/12/2022"]),
        ("Invalid date format: 031/02/2023.", []),
        ("Meeting scheduled for 30/09/2023.", ["30/09/2023"]),
        ("Dates: 01/01/2022, 02/02/2022, 03/03/2022", ["01/01/2022",
                                                       "02/02/2022",
                                                       "03/03/2022"]),
        ("No dates in this string.", []),
    ],
)
def test_find_dates(string, expected_result):
    assert find_dates(string) == expected_result
