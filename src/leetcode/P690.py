from typing import List


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        d = {}
        for employee in employees:
            d[employee.id] = employee

        def f(node):
            return d[node.id].importance + sum(f(d[s]) for s in node.subordinates)

        return f(d[id])
