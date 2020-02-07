import heapq

class HeadNode:
    def __init__(self, v, next):
        self.v = v
        self.next = next

    def __cmp__(self, other):
        return self.v - other.v

class Solution:

    def shortestSubarray(self, A, K):
        n = len(A)
        s = [0]
        for i in range(n):
            s.append(s[-1] + A[i])

        ans = -1
        l = 1
        r = n
        while l <= r:
            mid = (l + r) >> 1
            can = False
            for i in range(n - mid + 1):
                if s[mid + i] - s[i] >= K:
                    can = True
                    break
            ext = False
            f = 0
            ll = 0
            rr = 0
            last = None
            head = None
            heap = []
            for i in range(n):
                rr = i
                if f > 0:

                    f = f + A[i]
                    node = HeadNode(f, None)
                    if last is None:
                        head = node
                    if f >= K:
                        ext = True
                        break
                else:
                    ll = i
                    f = A[i]

            if can:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans


if __name__ == "__main__":
    print(Solution().shortestSubarray([44, -25, 75, -50, -38, -42, -32, -6, -40, -47], 19))
