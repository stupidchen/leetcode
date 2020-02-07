class Solution:
    def productExceptSelf(self, nums):
        l = [nums[0]]
        n = len(nums)
        for i in range(1, n):
            l.append(l[-1] * nums[i])
        r = [nums[-1]]
        for i in reversed(range(n - 1)):
            r.append(r[-1] * nums[i])
        ret = []
        for i in range(n):
            ll = l[i - 1] if i > 0 else 1
            rr = r[n - i - 2] if n - i - 2 >= 0 else 1
            ret.append(ll * rr)
        return ret

if __name__ == '__main__':
    print(Solution().productExceptSelf([1, 2]))