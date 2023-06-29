import pytest

from exercises.hackerrank import sorting

SAMPLE_CASE_0 = [5, [2, 3, 4, 2, 3, 6, 8, 4, 5], 2]
SAMPLE_CASE_1 = [4, [1, 2, 3, 4, 4], 0]
SAMPLE_CASE_2 = [3, [10, 20, 30, 40, 50], 1]


@pytest.mark.parametrize(
    "days,expenditure,expected", [SAMPLE_CASE_0, SAMPLE_CASE_1, SAMPLE_CASE_2]
)
def test_fraudulent_activity_notifications_sample_1(days, expenditure, expected):
    result = sorting.fraudulent_activity_notifications(
        expenditure=expenditure, days=days
    )

    assert result == expected
