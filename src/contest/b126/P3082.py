from typing import List

MODULO = 10 ** 9 + 7


class Solution:
    def sumOfPower(self, nums: List[int], k: int) -> int:
        n = len(nums)
        states = {(0, 0): 1}
        for num in nums:
            new_states = states.copy()
            for state in states:
                s, l = state
                if s + num > k:
                    continue
                new_states[(s + num, l + 1)] = new_states.get((s + num, l + 1), 0) + states[state]
            states = new_states

        res = 0
        for state, freq in states.items():
            s, l = state
            if s == k:
                res = (res + freq * (2 ** (n - l)) % MODULO) % MODULO
        return res


if __name__ == '__main__':
    r = Solution().sumOfPower(nums=[1, 2, 3], k=3)
    print(r)
