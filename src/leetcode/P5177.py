month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


class Solution:
    def reformatDate(self, date: str) -> str:
        d = date.split()

        dd = 0
        for i in range(len(d[0])):
            if d[0][i].isdigit():
                dd = dd * 10 + int(d[0][i])
            else:
                break

        dd = str(dd)
        if len(dd) < 2:
            dd = '0' + dd

        mm = str(month.index(d[1]) + 1)
        if len(mm) < 2:
            mm = '0' + mm

        yy = d[2]
        return "{}-{}-{}".format(yy, mm, dd)
