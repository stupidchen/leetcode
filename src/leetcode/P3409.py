class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if all([c.islower() for c in word]):
            return True
        if all([c.isupper() for c in word]):
            return True
        if word[0].isupper() and all([c.islower() for c in word[1:]]):
            return True
        return False
