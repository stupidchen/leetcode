class Solution:
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        flag = -1 if numerator * denominator < 0 else 1
        numerator = abs(numerator)
        denominator = abs(denominator)

        integer = numerator // denominator
        mod = numerator % denominator
        if mod == 0:
            return str(flag * integer)

        mod_map = {}
        div = []
        prefix = str(integer) + '.'
        if flag < 0:
            prefix = '-' + prefix
        while mod != 0:
            mod *= 10
            if mod in mod_map:
                return prefix + ''.join(div[:mod_map[mod]]) + '(' + ''.join(div[mod_map[mod]:]) + ')'
            div.append(str(mod // denominator))
            mod_map[mod] = len(div) - 1
            mod %= denominator
        return prefix + ''.join(div)

if __name__ == '__main__':
    print(Solution().fractionToDecimal(2, 3))
