class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: 'List[List[int]]') -> 'Node':
        is_leaf, val = self.is_leaf(grid)
        if is_leaf:
            return Node(val, is_leaf, None, None, None, None)

        n = len(grid)
        return Node(True, is_leaf,
                    self.construct([row[:n >> 1] for row in grid[:n >> 1]]),
                    self.construct([row[n >> 1:] for row in grid[:n >> 1]]),
                    self.construct([row[:n >> 1] for row in grid[n >> 1:]]),
                    self.construct([row[n >> 1:] for row in grid[n >> 1:]]),
                    )

    def is_leaf(self, grid: 'List[List[int]]'):
        s = sum([sum(row) for row in grid])
        if s == len(grid) * len(grid[0]) or s == 0:
            return True, s != 0
        else:
            return False, None
