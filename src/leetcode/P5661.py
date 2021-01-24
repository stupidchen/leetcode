class Solution:
    def maximumTime(self, time: str) -> str:
        r = ''
        if time[0] == '?':
            if time[1] < '4' or time[1] == '?':
                r += '2'
            else:
                r += '1'
        else:
            r += time[0]

        if time[1] == '?':
            if r[-1] == '2':
                r += '3'
            else:
                r += '9'
        else:
            r += time[1]

        r += ':'
        if time[3] == '?':
            r += '5'
        else:
            r += time[3]

        if time[4] == '?':
            r += '9'
        else:
            r += time[4]
        return r
