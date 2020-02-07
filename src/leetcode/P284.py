# Below is the interface for Iterator, which is already defined for you.
#
class Iterator:
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """
        self.i = 0
        self.nums = nums

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """
        return self.i < len(self.nums)

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """
        ret = self.nums[self.i]
        self.i += 1
        return ret

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iter = iterator
        self.last = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.last is None:
            self.last = self.iter.next()
        return self.last

    def next(self):
        """
        :rtype: int
        """
        if self.last is not None:
            ret = self.last
            self.last = None
            return ret
        return self.iter.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        return (self.last is not None) or self.iter.hasNext()


# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
if __name__ == '__main__':
    iter = PeekingIterator(Iterator([1, 2, 3]))
    print(iter.next())
    print(iter.peek())
    print(iter.next())
