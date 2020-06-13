class BrowserHistory:

    def __init__(self, homepage: str):
        self.a = [homepage]
        self.c = 0

    def visit(self, url: str) -> None:
        self.a = self.a[:self.c + 1] + [url]
        self.c = self.c + 1

    def back(self, steps: int) -> str:
        self.c -= steps
        if self.c < 0:
            self.c = 0
        return self.a[self.c]

    def forward(self, steps: int) -> str:
        self.c += steps
        if self.c >= len(self.a):
            self.c = len(self.a) - 1
        return self.a[self.c]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)