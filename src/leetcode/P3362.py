NEITHER = 'Neither'
IPV4 = 'IPv4'
IPV6 = 'IPv6'


class Solution:
    def validIPAddress(self, IP: str) -> str:
        if IP.find('.') != -1:
            a = IP.split('.')
            if len(a) == 4:
                for s in a:
                    if not s.isdigit() or int(s) < 0 or int(s) > 255 or (len(s) > 1 and s[0] == '0'):
                        return NEITHER
                return IPV4
            return NEITHER
        elif IP.find(':') != -1:
            symbols = '0123456789abcdefABCDEF'
            a = IP.split(':')
            if len(a) == 8:
                for s in a:
                    if len(s) == 0 or len(s) > 4 or any([c not in symbols for c in s]):
                        return NEITHER
                return IPV6
        return NEITHER
