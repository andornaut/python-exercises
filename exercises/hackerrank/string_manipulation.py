"""
https://www.hackerrank.com/interview/interview-preparation-kit/strings/challenges
"""


def sherlock_and_the_valid_string(sample: str) -> str:
    """
    https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem
    """
    sample = sorted(sample)  # type: ignore

    NO = "NO"
    YES = "YES"

    chars_to_repetitions = {}
    for char in sample:
        count = chars_to_repetitions.get(char, 0) + 1
        chars_to_repetitions[char] = count

    repetitions_to_count = {}
    for repetitions in chars_to_repetitions.values():
        count = repetitions_to_count.get(repetitions, 0) + 1
        repetitions_to_count[repetitions] = count

    chars_with_different_counts = len(repetitions_to_count)
    if chars_with_different_counts < 2:
        return YES
    if chars_with_different_counts > 2:
        return NO

    r1, r2 = repetitions_to_count.keys()
    c1, c2 = repetitions_to_count.values()

    if ((r1 - r2 == 1) or r1 == 1) and c1 == 1:
        return YES
    if ((r2 - r1 == 1) or r2 == 1) and c2 == 1:
        return YES
    return NO
