from functools import cmp_to_key


def compare(x, y):
    if x + y > y + x:
        return 1
    return -1


class Solution:
    def largestNumber(self, nums):
        if all(t == 0 for t in nums):
            return '0'
        tmp = [str(t) for t in nums]
        a = sorted(tmp, key=cmp_to_key(compare), reverse=True)
        return ''.join(a)

if __name__ == '__main__':
    print(Solution().largestNumber([3,30,34,5,9]))
