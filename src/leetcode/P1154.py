import datetime


class Solution:
    def dayOfYear(self, date):
        current_date = [int(x) for x in date.split('-')]
        year_start = datetime.date(current_date[0], 1, 1)
        return (datetime.date(current_date[0], current_date[1], current_date[2]) - year_start).days + 1
