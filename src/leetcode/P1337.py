class Solution:
    def kWeakestRows(self, mat, k):
        n, m = len(mat), len(mat[0])
        row = []
        for i in range(n):
            row.append((sum(mat[i]), i))
        row = sorted(row)
        return [r[1] for r in row[:k]]
