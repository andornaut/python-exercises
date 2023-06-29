import pytest

from exercises.hackerrank import search

SAMPLE_CASE_0 = [[1, 3, 5], [2, 3], [1, 2, 3], 8]
SAMPLE_CASE_1 = [[1, 4, 5], [2, 3, 3], [1, 2, 3], 5]
SAMPLE_CASE_2 = [[1, 3, 5, 7], [5, 7, 9], [7, 9, 11, 13], 12]


@pytest.mark.parametrize(
    "a,b,c,expected",
    [SAMPLE_CASE_0, SAMPLE_CASE_1, SAMPLE_CASE_2],
)
def test_triple_sum(a, b, c, expected):
    result = search.triple_sum(a, b, c)

    assert result == expected


@pytest.mark.skip(reason="Too slow")
@pytest.mark.lines_generator("triple_sum_test_case_2.txt")
def test_triple_sum_test_case_2(lines_generator):
    lines = lines_generator()
    a = list(map(int, next(lines).split()))
    b = list(map(int, next(lines).split()))
    c = list(map(int, next(lines).split()))

    result = search.triple_sum(a, b, c)

    assert result == 9593177511025
