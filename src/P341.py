# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.a = []
        for l in nestedList:
            t = l
            s = [[t, 0]]
            while len(s) != 0:
                if not s[-1][0].isInteger() and s[-1][1] < len(s[-1][0].getList()):
                    k = s[-1][1]
                    s[-1][1] += 1
                    s.append([(s[-1][0].getList())[k], 0])
                    continue
                if s[-1][0].isInteger():
                    self.a.append(s[-1][0].getInteger())
                s = s[:-1]
                continue
        self.i = 0

    def next(self):
        """
        :rtype: int
        """
        self.i += 1
        return self.a[self.i - 1]

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.i < len(self.a)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
