class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace(' ', '')
        number = number.replace('-', '')
        r = []
        while len(number) > 4:
            r.append(number[:3])
            number = number[3:]

        if len(number) == 4:
            r.append(number[:2])
            r.append(number[2:])
        else:
            r.append(number)

        return '-'.join(r)


if __name__ == '__main__':
    print(Solution().reformatNumber("1-23-45 6"))
