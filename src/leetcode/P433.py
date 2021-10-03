from typing import List

GENE = {'A', 'C', 'G', 'T'}

class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if start == end:
            return 0
        bank = {g: -1 for g in bank}
        n = len(start)
        q = [start]
        h = 0
        bank[start] = 0
        while h < len(q):
            cg, cs = q[h], bank[q[h]]
            for i in range(n):
                for g in GENE:
                    if cg[i] != g:
                        ng = cg[:i] + g + cg[i+1:]
                        if ng in bank and bank[ng] == -1:
                            if ng == end:
                                return cs + 1
                            bank[ng] = cs + 1
                            q.append(ng)
            h += 1
        return -1
