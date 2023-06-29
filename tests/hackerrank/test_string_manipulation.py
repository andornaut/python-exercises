import pytest

from exercises.hackerrank import string_manipulation

SAMPLE_CASE_0 = ["aabbcd", "NO"]
SAMPLE_CASE_1 = ["aabbccddeefghi", "NO"]
SAMPLE_CASE_2 = ["abcdefghhgfedecba", "YES"]
ONE_CHAR = ["a", "YES"]
ONE_CHAR_REPEATED_AND_ANOTHER = ["aaaaaaaaab", "YES"]
ONE_CHAR_REPEATED_AND_TWO_OTHERS = ["aaaaaaaaabc", "NO"]


@pytest.mark.parametrize(
    "sample,expected",
    [
        SAMPLE_CASE_0,
        SAMPLE_CASE_1,
        SAMPLE_CASE_2,
        ONE_CHAR,
        ONE_CHAR_REPEATED_AND_ANOTHER,
        ONE_CHAR_REPEATED_AND_TWO_OTHERS,
    ],
)
def test_sherlock_and_the_valid_string(sample, expected):
    result = string_manipulation.sherlock_and_the_valid_string(sample)

    assert result == expected
