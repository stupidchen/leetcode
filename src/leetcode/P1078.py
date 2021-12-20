class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        words = text.split()
        r = []
        for i in range(2, len(words)):
            if words[i - 2] == first and words[i - 1] == second:
                r.append(words[i])
        return r
