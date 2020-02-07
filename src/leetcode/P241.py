class Solution:
    def diffWaysToCompute(self, input: 'str') -> 'List[int]':
        if input.isdigit():
            return [int(input)]

        ret = []
        for i in range(len(input)):
            if input[i] in '+-*':
                ret1 = self.diffWaysToCompute(input[:i])
                ret2 = self.diffWaysToCompute(input[i+1:])
                for op1 in ret1:
                    for op2 in ret2:
                        if input[i] == '+':
                            ret.append(op1 + op2)
                        elif input[i] == '-':
                            ret.append(op1 - op2)
                        elif input[i] == '*':
                            ret.append(op1 * op2)
        return ret


if __name__ == '__main__':
    print(Solution().diffWaysToCompute("2*3-4*5"))
