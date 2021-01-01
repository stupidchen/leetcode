class Solution:
    def canFormArray(self, arr, pieces):
        i = 0
        n = len(arr)
        m = len(pieces)
        v = [False] * m
        while i < n:
            t = -1
            for j in range(m):
                if not v[j] and arr[i] == pieces[j][0]:
                    t = j
                    break
            if t == -1:
                return False
            v[t] = True
            for k in range(len(pieces[t])):
                if pieces[t][k] == arr[i]:
                    i += 1
                else:
                    return False
        return True


if __name__ == '__main__':
    print(Solution().canFormArray(arr=[91, 78], pieces=[[78], [4, 64], [91]]))
    print(Solution().canFormArray(arr=[91, 4, 64, 78], pieces=[[78], [4, 64], [91]]))
