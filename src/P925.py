class Solution:
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        i, j = 0, 0
        n, m = len(name), len(typed)
        while i < n and j < m:
            if name[i] != typed[j]:
                return False
            if i >= n - 1 or name[i] != name[i + 1]:
                while j < m and name[i] == typed[j]:
                    j += 1
            else:
                j += 1
            i += 1
        return i == n and j == m

if __name__ == '__main__':
    print(Solution().isLongPressedName('vtkgn', 'vttkgnn'))
