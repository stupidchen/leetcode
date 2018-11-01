VOWELS = 'aeiouAEIOU'

class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        v = []
        for c in s:
            if c in VOWELS:
                v.append(c)
        ret = ''
        i = -1
        for c in s:
            if c in VOWELS:
                ret += v[i]
                i -= 1
            else:
                ret += c
        return ret

if __name__ == '__main__':
    print(Solution().reverseVowels('hello'))
