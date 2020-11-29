class Solution:
    def canReach(self, arr, start: int):
        n = len(arr)
        v = [False] * n
        q = [start]
        v[start] = True
        h = 0
        while h < len(q):
            if arr[q[h]] == 0:
                return True

            t = q[h] - arr[q[h]]
            if 0 <= t < n and not v[t]:
                q.append(t)
                v[t] = True

            t = q[h] + arr[q[h]]
            if 0 <= t < n and not v[t]:
                q.append(t)
                v[t] = True

            h += 1
        return False
