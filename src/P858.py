class Solution:
    def mirrorReflection(self, p, q):
        s = 2
        c = [-1, 0, 1, 2]
        while p % q != 0:
            t = p % q
            if (p // q) % 2 == 0:
                c = [c[0], c[3], c[2], c[1]]
            else:
                c = [c[1], c[2], c[3], c[0]]
            q = t
        return c[3 - (p // q) % 2]


if __name__ == "__main__":
    print(Solution().mirrorReflection(3, 2))
