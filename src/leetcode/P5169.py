import datetime

class Solution:
    def daysBetweenDates(self, date1, date2):
        d1, d2 = datetime.datetime.strptime(date1, '%Y-%m-%d'), datetime.datetime.strptime(date2, '%Y-%m-%d')
        d = d2 - d1
        return abs(d.days)

if __name__ == '__main__':
    print(Solution().daysBetweenDates("2020-01-15", "2019-12-31"))
