class Solution:
    def reconstructQueue(self, people: 'List[List[int]]') -> 'List[List[int]]':
        people = sorted(people, key=lambda p: (-p[0], p[1]))
        ret = []
        for p in people:
            ret.insert(p[1], p)
        return ret
