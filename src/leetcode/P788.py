class Solution:
    def rotatedDigits(self, N: int) -> int:
        invalid, rotate = set(str(347)), set(str(2569))
        return sum([1 for s in map(lambda i: set(str(i)), range(1, N + 1)) if not s & invalid and s & rotate])
