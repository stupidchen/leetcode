class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        s = '[' + s + ']'
        for c in s:
            if c == '[':
                stack.append(c)
            elif c.isdigit():
                if len(stack) == 0 or not isinstance(stack[-1], int):
                    stack.append(0)
                stack[-1] = stack[-1] * 10 + (ord(c) - ord('0'))
            elif c.isalpha():
                if len(stack) == 0 or not (isinstance(stack[-1], str) and stack[-1].isalpha()):
                    stack.append('')
                stack[-1] += c
            else:
                # Deal with ]
                p = ''
                while stack[-1] != '[':
                    p = stack.pop() + p
                stack.pop()
                if len(stack) > 0 and isinstance(stack[-1], int):
                    n = stack.pop()
                else:
                    n = 1
                stack.append(''.join([p] * n))
        return stack[0]


if __name__ == '__main__':
    print(Solution().decodeString('[abc][cd]ef'))
