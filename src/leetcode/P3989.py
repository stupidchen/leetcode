class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        d = set()
        for email in emails:
            name = email.split('@')
            host = name[0]
            plus = host.split('+')
            host = plus[0].replace('.', '')
            d.add(f'{host}@{name[1]}')
        return len(d)


if __name__ == '__main__':
    print(Solution().numUniqueEmails(["test.email+alex@leetcode.com", "test.email.leet+alex@code.com"]))
