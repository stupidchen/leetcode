class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) > len(str2):
            return self.gcdOfStrings(str2, str1)

        if str1 == '':
            return str2

        if str2[:len(str1)] == str1:
            r = str2[len(str1):]
            return self.gcdOfStrings(r, str1)
        else:
            return ''

