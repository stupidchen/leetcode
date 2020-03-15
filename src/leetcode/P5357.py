class CustomStack:

    def __init__(self, maxSize: int):
        self.s = []
        self.m = maxSize

    def push(self, x: int) -> None:
        if len(self.s) < self.m:
            self.s.append(x)

    def pop(self) -> int:
        if len(self.s) == 0:
            return -1
        else:
            return self.s.pop()

    def increment(self, k: int, val: int) -> None:
        for i in range(min(len(self.s), k)):
            self.s[i] += val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
