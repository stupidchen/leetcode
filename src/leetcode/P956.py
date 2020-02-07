from functools import lru_cache


class Solution(object):
    def tallestBillboard(self, rods):
        """
        :type rods: List[int]
        :rtype: int
        """
        @lru_cache(None)
        def f(i, s):
            if i == len(rods):
                return 0 if s == 0 else -2147483647

            return max(f(i + 1, s),
                       f(i + 1, s - rods[i]),
                       f(i + 1, s + rods[i]) + rods[i]
                       )

        return f(0, 0)


if __name__ == '__main__':
    print(Solution().tallestBillboard([1,2,4,8,16,32,64,128,256,512,50,50,50,150,150,150,100,100,100,123]))
