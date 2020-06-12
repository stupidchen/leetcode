MOD = 10 ** 9 + 7


class Solution:
    def maxArea(self, h, w, horizontalCuts, verticalCuts) -> int:
        horizontalCuts.append(0)
        horizontalCuts.append(h)
        verticalCuts.append(0)
        verticalCuts.append(w)
        horizontalCuts = sorted(horizontalCuts)
        verticalCuts = sorted(verticalCuts)

        mh = 0
        mv = 0
        for i in range(len(horizontalCuts) - 1):
            mh = max(horizontalCuts[i + 1] - horizontalCuts[i], mh)
        for i in range(len(verticalCuts) - 1):
            mv = max(verticalCuts[i + 1] - verticalCuts[i], mv)
        return mh * mv % MOD


if __name__ == '__main__':
    print(Solution().maxArea(h=5, w=4, horizontalCuts=[3, 1], verticalCuts=[1]))
