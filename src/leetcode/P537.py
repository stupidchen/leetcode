class Solution:
    def complexNumberMultiply(self, num1, num2):
        p1, p2 = num1.split('+')
        n1 = complex(int(p1), int(p2[:-1]))

        p1, p2 = num2.split('+')
        n2 = complex(int(p1), int(p2[:-1]))
        n1 = n1 * n2
        return str(int(n1.real)) + '+' + str(int(n1.imag)) + 'i'


if __name__ == '__main__':
    print(Solution().complexNumberMultiply(num1="1+-1i", num2="1+-1i"))
