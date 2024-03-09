from typing import List


class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        res = 0
        for i, alice in enumerate(points):
            for j, bob in enumerate(points):
                if i != j and alice[0] >= bob[0] and alice[1] <= bob[1]:
                    someone_inside = False
                    for k, others in enumerate(points):
                        if i != k and j != k:
                            if bob[0] <= others[0] <= alice[0] and alice[1] <= others[1] <= bob[1]:
                                someone_inside = True
                                break
                    if not someone_inside:
                        res += 1
        return res

