class Solution:
    def addToArrayForm(self, A: 'List[int]', K: 'int') -> 'List[int]':
        b = []
        while K > 0:
            b.append(K % 10)
            K = K // 10

        a = list(reversed(A))
        while len(a) < len(b):
            a.append(0)
        while len(a) > len(b):
            b.append(0)
        a.append(0)
        b.append(0)
        k = 0
        i = 0
        while i < len(b) or k != 0:
            a[i] = k + a[i] + b[i]
            if a[i] >= 10:
                a[i] -= 10
                k = 1
            else:
                k = 0
            i += 1

        if a[-1] == 0 and len(a) > 1:
            a = a[:-1]
        return list(reversed(a))


if __name__ == '__main__':
    print(Solution().addToArrayForm([0, 0, 0], 0))
