class Solution:
    def calculate(self, s: 'str') -> 'int':
        s.replace(' ', '')
        s += '#'
        op, num = '#+-*/', '0123456789'
        tokens = []
        token = ''
        for c in s:
            if c in op:
                if token != '':
                    tokens.append(int(token))
                    token = ''
                tokens.append(c)
            else:
                token += c

        def level(opc):
            return (op.find(opc) + 1) >> 1

        os, ns = [], []
        for token in tokens:
            if isinstance(token, str):
                while len(os) > 0 and level(token) <= level(os[-1]):
                    num2, num1 = ns.pop(-1), ns.pop(-1)
                    o = os.pop(-1)
                    if o == '+':
                        ns.append(num1 + num2)
                    elif o == '-':
                        ns.append(num1 - num2)
                    elif o == '*':
                        ns.append(num1 * num2)
                    elif o == '/':
                        ns.append(num1 // num2)
                os.append(token)
            else:
                ns.append(token)
        if len(ns) > 0:
            return ns[-1]
        else:
            return 0


if __name__ == '__main__':
    print(Solution().calculate("328+233*22/2-17+81*21-5*6"))
