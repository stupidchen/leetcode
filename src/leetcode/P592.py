import fractions


def do_math(x, y, o):
    if o == '+':
        return x + y
    elif o == '-':
        return x - y


class Solution:
    def fractionAddition(self, expression: str) -> str:
        r = fractions.Fraction(0, 1)
        expression += '+0/1'
        op = '+'
        op_n = 0
        op_no = [0, 0]
        for c in expression:
            if c == '+':
                if op_n == 0:
                    op = c
                    continue
                r = do_math(r, fractions.Fraction(*op_no), op)
                op = c
                op_n = 0
                op_no = [0, 0]
            elif c == '-':
                if op_n == 0:
                    op = c
                    continue
                r = do_math(r, fractions.Fraction(*op_no), op)
                op = c
                op_n = 0
                op_no = [0, 0]
            elif c == '/':
                op_n = 1
            else:
                op_no[op_n] = op_no[op_n] * 10 + int(c)
        return '/'.join(map(str, r.as_integer_ratio()))


if __name__ == '__main__':
    print(Solution().fractionAddition("1/3-1/2"))
