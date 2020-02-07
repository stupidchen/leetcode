class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        d = {}
        for email in emails:
            name = email.split('@')
            host = name[0]
            plus = host.split('+')
            realhost = plus[0].replace('.', '')
            d[realhost + name[1]] = 1
        return len(d.keys())

if __name__ == '__main__':
    print(Solution().numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))
