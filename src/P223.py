class Solution:
    def intersectCheck(self, A, B, C, D, E, F, G, H):
        ret = (D - B) * (C - A) + (H - F) * (G - E)
        i = False
        if E >= C or G <= A:
            return ret, i
        x = min(G, C) - max(A, E)
        if H <= B or F >= D:
            return ret, i
        y = min(H, D) - max(F, B)
        i = True
        return ret - x * y, i

    def computeArea(self, A, B, C, D, E, F, G, H):
        area, inter = self.intersectCheck(A, B, C, D, E, F, G, H)
        if inter:
            return area
        area, inter = self.intersectCheck(E, F, G, H, A, B, C, D)
        return area


if __name__ == '__main__':
    print(Solution().computeArea(-2, -2, 2, 2, -2, -2, 2, 2))
