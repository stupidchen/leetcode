class Solution:
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        ret = []

        def solve(num, last, exp, val):
            if not num:
                if val == target:
                    ret.append(exp)
                return

            for i in range(1, len(num) + 1):
                if i == 1 or (i > 1 and num[0] != '0'):
                    new_val = num[:i]
                    solve(num[i:], last * int(new_val), exp + '*' + new_val, val - last + last * int(new_val))
                    solve(num[i:], -int(new_val), exp + '-' + new_val, val - int(new_val))
                    solve(num[i:], int(new_val), exp + '+' + new_val, val + int(new_val))

        for i in range(1, len(num) + 1):
            if i == 1 or (i > 1 and num[0] != '0'):
                solve(num[i:], int(num[:i]), num[:i], int(num[:i]))
        return ret
