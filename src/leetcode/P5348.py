class Solution:
    def findTheDistanceValue(self, arr1, arr2, d):
        r = 0
        for a in arr1:
            c = True
            for b in arr2:
                if abs(a - b) <= d:
                    c = False
                    break
            if c:
                r += 1
        return r


if __name__ == '__main__':
    print(Solution().findTheDistanceValue(arr1=[2, 1, 100, 3], arr2=[-5, -2, 10, -3, 7], d=6))
