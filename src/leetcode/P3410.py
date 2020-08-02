SIZE = 100000


class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.h = [[] for i in range(SIZE)]

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.h[key % SIZE].append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.h[key % SIZE].remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return key in self.h[key % SIZE]


if __name__ == '__main__':
    s = MyHashSet()
    s.add(1)
    s.add(2)
    print(s.contains(2))
    s.add(2)
    print(s.contains(2))
    s.remove(2)
    print(s.contains(2))

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
