OPERATOR = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: int(a / b),
}


class Solution:
    def evalRPN(self, tokens):
        stack = []
        for token in tokens:
            if len(token) > 1 or token.isdigit():
                stack.append(int(token))
            else:
                op1 = stack.pop(-1)
                op2 = stack.pop(-1)
                stack.append(OPERATOR[token](op2, op1))
        return stack[0]


if __name__ == '__main__':
    print(Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
