class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        return all([ransomNote.count(i) <= magazine.count(i) for i in set(ransomNote)])