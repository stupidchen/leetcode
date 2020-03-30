class Solution:
    def PredictTheWinner(self, nums):
        def predict(l, r, s, t):
            if l == r:
                return s[0] >= s[1]

            u = [s[0], s[1]]
            u[t] += nums[l]
            v = [s[0], s[1]]
            v[t] += nums[r - 1]

            if t == 0:
                return predict(l + 1, r, u, 1 - t) or predict(l, r - 1, v, 1 - t)
            else:
                return predict(l + 1, r, u, 1 - t) and predict(l, r - 1, v, 1 - t)

        return predict(0, len(nums), [0, 0], 0)


if __name__ == '__main__':
    print(Solution().PredictTheWinner([1, 5, 233, 7]))
