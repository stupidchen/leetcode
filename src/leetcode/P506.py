from typing import List

DATA = {
    0: 'Gold Medal',
    1: 'Silver Medal',
    2: 'Bronze Medal'
}


def convert_rank(x):
    return DATA.get(x, str(x + 1))


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        score_data = sorted([(s, i) for i, s in enumerate(score)], reverse=True)
        rank = [''] * len(score_data)
        for i, sd in enumerate(score_data):
            rank[sd[1]] = convert_rank(i)
        return rank
