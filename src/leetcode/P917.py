class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        n = len(S)
        i = 0
        j = n - 1
        while i < j:
            while i < j and not S[i].isalpha():
                i += 1
            while i < j and not S[j].isalpha():
                j -= 1
            if i < j and S[i].isalpha() and S[j].isalpha():
                S = S[:i] + S[j] + S[i + 1: j] + S[i] + S[j + 1:]
            i += 1
            j -= 1
        return S


if __name__ == '__main__':
    print(Solution().reverseOnlyLetters('a-bC-dEf-ghIj'))
