"""
https://www.hackerrank.com/interview/interview-preparation-kit/search/challenges
"""


def triple_sum(a: list[int], b: list[int], c: list[int]):
    """
    https://www.hackerrank.com/challenges/triple-sum/problem
    """
    a = list(set(a))
    b = list(set(b))
    c = list(set(c))

    a.sort()
    b.sort(reverse=True)
    c.sort()

    count = 0
    for p in a:
        for q in b:
            if p > q:
                break
            for r in c:
                if r > q:
                    break
                count += 1
    return count
