from random import randint
from typing import List


class Solution:

    def __init__(self, m: int, n: int):
        self._ones = set()
        self._n = n
        self._m = m
        self._size = n * m

    def flip(self) -> List[int]:
        ones = self._ones
        p = self._pick()
        while p in ones:
            p = self._pick()
        ones.add(p)
        return list(divmod(p, self._n))

    def _pick(self):
        size = self._size
        f = randint(0, size - 1)
        return f

    def reset(self) -> None:
        self._ones = set()
