def find_loop(x, l, r, f):
    if x == -1:
        return False
    if f[x]:
        return True

    f[x] = True
    return find_loop(l[x], l, r, f) or find_loop(r[x], l, r, f)


def find(x, v):
    if x != v[x]:
        v[x] = find(v[x], v)
    return v[x]


def merge(x, y, v):
    vx = find(x, v)
    vy = find(y, v)
    v[vx] = vy


class Solution:
    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        for i in range(n):
            f = [False] * n
            if find_loop(i, leftChild, rightChild, f):
                return False

        v = [i for i in range(n)]
        for i in range(n):
            if leftChild[i] != -1:
                merge(leftChild[i], i, v)
            if rightChild[i] != -1:
                merge(rightChild[i], i, v)
        t = find(0, v)
        return all(find(i, v) == t for i in range(n))


if __name__ == '__main__':
    print(Solution().validateBinaryTreeNodes(n=6, leftChild=[1, -1, -1, 4, -1, -1], rightChild=[2, -1, -1, 5, -1, -1]))
    print(Solution().validateBinaryTreeNodes(n=4, leftChild=[1, -1, 3, -1], rightChild=[2, -1, -1, -1]))
    print(Solution().validateBinaryTreeNodes(n=4, leftChild=[1, -1, 3, -1], rightChild=[2, 3, -1, -1]))
    print(Solution().validateBinaryTreeNodes(n=2, leftChild=[1, 0], rightChild=[-1, -1]))
