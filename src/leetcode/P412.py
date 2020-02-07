class Solution:
    def fizzBuzz(self, n: 'int') -> 'List[str]':
        name = [
            (3, 'Fizz'),
            (5, 'Buzz'),
            (15, 'FizzBuzz'),
        ]
        ret = []
        for i in range(1, n + 1):
            found = False
            for pair in reversed(name):
                if i % pair[0] == 0:
                    found = True
                    ret.append(pair[1])
                    break
            if not found:
                ret.append(str(i))
        return ret
