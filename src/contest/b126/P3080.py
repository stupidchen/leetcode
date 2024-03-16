from collections import Counter, defaultdict
from typing import List


class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        c = Counter(nums)
        counter = defaultdict(lambda: [])
        count = {}
        for i, num in enumerate(nums):
            counter[num].append(i)
            count[num] = 0
        sorted_nums = sorted(c.keys())
        m = len(sorted_nums)
        res = []
        num_sum = sum(nums)
        marked = [False] * n
        smallest_index = 0
        for query in queries:
            index, k = query
            if not marked[index]:
                marked[index] = True
                num_sum -= (num := nums[index])

            for i in range(k):
                while smallest_index < m:
                    smallest = sorted_nums[smallest_index]
                    while count[smallest] < len(counter[smallest]) and marked[counter[smallest][count[smallest]]]:
                        count[smallest] += 1
                    if count[smallest] < len(counter[smallest]):
                        break
                    smallest_index += 1

                if smallest_index == m:
                    break

                marked[counter[smallest][count[smallest]]] = True
                num_sum -= smallest
                count[smallest] += 1

            res.append(num_sum)
        return res


if __name__ == '__main__':
    r = Solution().unmarkedSumArray([15, 15, 20, 15, 14, 14, 13, 17, 13, 14, 1, 15, 15, 14, 18, 1, 16, 4, 9, 20],
                                    [[11, 3], [10, 4], [12, 4], [18, 4], [9, 2], [16, 4], [9, 3], [15, 1], [13, 4],
                                     [17, 1], [8, 2], [0, 2], [4, 1], [14, 0], [19, 1]])
    print(r)
