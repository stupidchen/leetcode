class Foo:
    def __init__(self):
        self.lock = 0

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.lock = 1

    def second(self, printSecond: 'Callable[[], None]') -> None:
        # printSecond() outputs "second". Do not change or remove this line.
        while self.lock < 1:
            continue
        printSecond()
        self.lock = 2

    def third(self, printThird: 'Callable[[], None]') -> None:
        # printThird() outputs "third". Do not change or remove this line.
        while self.lock < 2:
            continue
        printThird()
