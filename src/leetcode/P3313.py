from collections import Counter


class FirstUnique:

    def __init__(self, nums):
        self.h = [-2, -1]
        self.c = Counter(nums)
        t = -1
        self.l = {-1: self.h}
        for num in nums:
            if self.c[num] == 1:
                n = [t, -1]
                self.l[t][1] = num
                self.l[num] = n
                t = num
        self.t = t

    def showFirstUnique(self) -> int:
        return self.h[1]

    def add(self, value: int) -> None:
        self.c[value] += 1
        if self.c[value] == 1:
            n = [self.t, -1]
            self.l[self.t][1] = value
            self.l[value] = n
            self.t = value
        elif self.c[value] == 2:
            c = self.l[value]
            if c[0] != -2:
                self.l[c[0]][1] = c[1]
            if c[1] != -1:
                self.l[c[1]][0] = c[0]
            if self.t == value:
                self.t = c[0]


if __name__ == '__main__':
    nums = [2, 3, 5]
    obj = FirstUnique(nums)
    print(obj.showFirstUnique())
    obj.add(5)
    print(obj.showFirstUnique())
    obj.add(2)
    print(obj.showFirstUnique())
    obj.add(3)
    print(obj.showFirstUnique())
    obj.add(4)
    print(obj.showFirstUnique())

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
