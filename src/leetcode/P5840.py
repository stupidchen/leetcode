class Solution:
    def minSwaps(self, s):
        stack = []
        for c in s:
            if c == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(']')
            else:
                stack.append('[')
        return ((len(stack) >> 1) + 1) >> 1
