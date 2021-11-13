from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        f = []
        ret = [0] * n
        for i in reversed(range(n)):
            t = temperatures[i]
            while f:
                if f[-1][0] > t:
                    ret[i] = f[-1][1] - i
                    break
                else:
                    f.pop()
            f.append((t, i))

        return ret


if __name__ == '__main__':
    print(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
