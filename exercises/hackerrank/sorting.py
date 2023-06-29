"""
https://www.hackerrank.com/interview/interview-preparation-kit/sorting/challenges
"""
from bisect import insort
from dataclasses import dataclass
from functools import reduce


def fraudulent_activity_notifications(expenditure, days):
    """
    https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem
    """

    @dataclass
    class State:
        prev_exp: int
        next_exp: int
        index: int

    SENTINEL_EXP = -1
    state = State(SENTINEL_EXP, SENTINEL_EXP, 0)
    middle_pos = int(days / 2)
    sorted_window = sorted(expenditure[:days])

    def incremental_median(prev_exp, next_exp):
        # Incremental implementation of `statistics.median`
        if prev_exp != SENTINEL_EXP:
            sorted_window.remove(prev_exp)
            insort(sorted_window, next_exp)
        result = sorted_window[middle_pos]
        if days % 2 == 0:
            result += sorted_window[middle_pos - 1]
            result /= 2
        return result

    def notify(aggregator, exp):
        median = incremental_median(state.prev_exp, state.next_exp)
        state.prev_exp = expenditure[state.index]
        state.next_exp = exp
        state.index += 1
        if exp >= (median * 2):
            aggregator += 1
        return aggregator

    return reduce(notify, expenditure[days:], 0)
