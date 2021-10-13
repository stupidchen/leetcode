from typing import List


class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)

        def get_next_index(idx, direction):
            if idx == -1 or nums[idx] == 0:
                return -1
            if nums[idx] * direction < 0:
                return -1

            next_idx = (nums[idx] + idx) % n
            return next_idx if next_idx != idx else -1

        for i in range(n):
            d = 1 if nums[i] > 0 else -1
            slow = get_next_index(i, d)
            fast = get_next_index(get_next_index(i, d), d)
            while slow != fast and slow != -1 and fast != -1:
                slow = get_next_index(slow, d)
                fast = get_next_index(get_next_index(fast, d), d)
            if slow != -1 and fast == slow:
                return True
            nums[i] = 0
        return False


if __name__ == '__main__':
    print(Solution().circularArrayLoop([2,-1,1,2,2]))
