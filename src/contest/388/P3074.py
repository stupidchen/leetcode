from typing import List


class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        t = sum(apple)
        capacity.sort(key=lambda x: -x)
        res = 0
        for box in capacity:
            res += 1
            t -= box
            if t <= 0:
                break
        return res


if __name__ == '__main__':
    r = Solution()
    print(r)
