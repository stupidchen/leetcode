class Solution:
    def validSquare(self, p1, p2, p3, p4) -> bool:
        def distance(v1, v2):
            return (v1[0] - v2[0]) ** 2 + (v1[1] - v2[1]) ** 2

        def cross_product(v1, v2):
            return v1[0] * v2[0] + v1[1] * v2[1]

        def vector(v1, v2):
            return v1[0] - v2[0], v1[1] - v2[1]

        def valid(v1, v2, v3, v4):
            if distance(v1, v2) == distance(v3, v4) == distance(v2, v3):
                if cross_product(vector(v1, v2), vector(v2, v3)) == 0 and cross_product(vector(v2, v3),
                                                                                        vector(v3, v4)) == 0:
                    return True
            return False

        if p1 == p2 or p1 == p3 or p1 == p4:
            return False

        return valid(p1, p2, p3, p4) or valid(p1, p2, p4, p3) or valid(p1, p3, p2, p4) or valid(p1, p3, p4, p2) \
               or valid(p1, p4, p2, p3) or valid(p1, p4, p3, p2)


if __name__ == '__main__':
    print(Solution().validSquare([0, 0], [5, 0], [5, 4], [0, 4]))
