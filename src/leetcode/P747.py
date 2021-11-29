class Solution:
    def dominantIndex(self, nums):
        max_index = -1
        largest = max(nums)
        for i in range(len(nums)):
            if nums[i] == largest:
                max_index = i
            elif largest < (nums[i] << 1):
                return -1
        return max_index


if __name__ == '__main__':
    print(Solution().dominantIndex([3, 6, 1, 0]))
