class Solution:
    def average(self, salary) -> float:
        return (sum(salary) - min(salary) - max(salary)) / (len(salary) - 2)
