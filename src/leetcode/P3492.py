class Solution:
    def buddyStrings(self, A, B):
        if len(A) != len(B):
            return False
        di = []
        s = {}
        t = False
        for i in range(len(A)):
            if A[i] != B[i]:
                di.append(i)
                if len(di) > 2:
                    return False
            else:
                s[A[i]] = s.setdefault(A[i], 0) + 1
                if s[A[i]] > 1:
                    t = True
        if len(di) == 0:
            return t
        if len(di) == 1:
            return False
        if A[di[0]] == B[di[1]] and A[di[1]] == B[di[0]]:
            return True
        return False
