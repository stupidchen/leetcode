class Solution:
    def secondHighest(self, s: str) -> int:
        numbers = set()
        for c in s:
            if c.isdigit():
                numbers.add(c)
        numbers = sorted(numbers)
        return numbers[-2] if len(numbers) >= 2 else -1

