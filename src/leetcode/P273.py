O = ['Zero ', 'One ', 'Two ', 'Three ', 'Four ', 'Five ', 'Six ', 'Seven ', 'Eight ', 'Nine ', 'Ten ', 'Eleven ',
     'Twelve ', 'Thirteen ', 'Fourteen ', 'Fifteen ', 'Sixteen ', 'Seventeen ', 'Eighteen ', 'Nineteen ']
T = ['Twenty ', 'Thirty ', 'Forty ', 'Fifty ', 'Sixty ', 'Seventy ', 'Eighty ', 'Ninety ']


class Solution:
    @staticmethod
    def solve(num: int) -> str:
        r = ''
        if num >= 10 ** 9:
            t = num // 10 ** 9
            r += O[t] + 'Billion '
            num %= 10 ** 9

        if num >= 10 ** 6:
            t = num // 10 ** 6
            r += Solution().numberToWords(t) + ' Million '
            num %= 10 ** 6

        if num >= 10 ** 3:
            t = num // 10 ** 3
            r += Solution().numberToWords(t) + ' Thousand '
            num %= 10 ** 3

        if num >= 100:
            t = num // 100
            r += Solution().numberToWords(t) + ' Hundred '
            num %= 100

        if num >= 20:
            t = num // 10
            num %= 10
            r += T[t - 2]
            if num != 0:
                r += O[num]
        elif num > 0:
            r += O[num]

        return r[:-1]

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return O[0][:-1]
        else:
            return Solution.solve(num)


# For test only
SI = ((100,), (0,), (1234567891,), (123,), (12345,), (1234567,))
SO = ("One Hundred", "Zero",
      "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One",
      "One Hundred Twenty Three", "Twelve Thousand Three Hundred Forty Five",
      "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven")
TM = 'numberToWords'
if __name__ == '__main__':
    from leetcode.PTester import PTester

    PTester(SI, SO, Solution, TM).run()
