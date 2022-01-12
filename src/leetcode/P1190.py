class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for c in s:
            if c == ')':
                t = ''
                while stack:
                    g = stack.pop()
                    if g == '(':
                        break
                    t = g + t
                if t:
                    t = t[::-1]
                stack.append(t)
            elif c == '(':
                stack.append(c)
            else:
                if not stack or stack[-1] == '(':
                    stack.append('')
                stack[-1] = stack[-1] + c
        return ''.join(stack)


if __name__ == '__main__':
    print(Solution().reverseParentheses('(a(bc))'))
