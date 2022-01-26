from enum import Enum
from threading import Lock


class FuncType(Enum):
    fizz = 0
    buzz = 1
    fizzbuzz = 2
    number = 3

class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.locks = {
            FuncType.fizz: Lock(),
            FuncType.buzz: Lock(),
            FuncType.fizzbuzz: Lock(),
            FuncType.number: Lock(),
        }
        self.locks[FuncType.fizz].acquire()
        self.locks[FuncType.buzz].acquire()
        self.locks[FuncType.fizzbuzz].acquire()

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        for i in range(self.n):
            t = i + 1
            if t % 3 == 0 and t % 5 != 0:
                self.locks[FuncType.fizz].acquire()
                printFizz()
                self.locks[FuncType.number].release()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        for i in range(self.n):
            t = i + 1
            if t % 3 != 0 and t % 5 == 0:
                self.locks[FuncType.buzz].acquire()
                printBuzz()
                self.locks[FuncType.number].release()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        for i in range(self.n):
            t = i + 1
            if t % 3 == 0 and t % 5 == 0:
                self.locks[FuncType.fizzbuzz].acquire()
                printFizzBuzz()
                self.locks[FuncType.number].release()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(self.n):
            t = i + 1
            self.locks[FuncType.number].acquire()
            if t % 3 == 0 and t % 5 == 0:
                self.locks[FuncType.fizzbuzz].release()
            elif t % 3 == 0:
                self.locks[FuncType.fizz].release()
            elif t % 5 == 0:
                self.locks[FuncType.buzz].release()
            else:
                printNumber(t)
                self.locks[FuncType.number].release()
