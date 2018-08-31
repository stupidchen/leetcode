class Solution(object):
    def majorityElement(self, nums):
        candidate1 = 0
        candidate2 = 0
        count1 = 0
        count2 = 0
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1, count2 = count1 - 1, count2 - 1

        if candidate1 == candidate2:
            tmp = [candidate1]
        else:
            tmp = (candidate1, candidate2)
        return [num for num in tmp if nums.count(num) > len(nums) // 3]

if __name__ == '__main__':
    print(Solution().majorityElement([1,2]))