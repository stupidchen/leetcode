class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.a = [i for i in range(combinationLength)]
        self.a[-1] -= 1
        self.m = combinationLength
        self.n = len(characters)
        self.c = characters

    def next(self) -> str:

        i = -1
        for j in reversed(range(self.m)):
            if self.a[j] < self.n - self.m + j:
                i = j
                break

        if i != -1:
            self.a[i] += 1
            for j in range(i + 1, self.m):
                self.a[j] = self.a[j - 1] + 1
            ret = ''.join([self.c[i] for i in self.a])
        else:
            ret = ''
        return ret

    def hasNext(self) -> bool:
        return self.a != [i for i in range(self.n - self.m, self.n)]


if __name__ == '__main__':
    c = CombinationIterator('abc', 2)
    print(c.next())
    print(c.hasNext())
    print(c.next())
    print(c.hasNext())
    print(c.next())
    print(c.hasNext())
    print(c.next())

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
