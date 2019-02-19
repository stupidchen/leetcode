class Solution:
    def isValid(self, S: str) -> bool:
        if 'a' not in S or 'b' not in S or 'c' not in S:
            return False
        st = []
        for c in S:
            if c == 'a' or c == 'b':
                st.append(c)
                continue
            if c == 'c':
                p = 0
                while len(st) > 0 and st[-1] != 'a':
                    t = st.pop()
                    if t != 'b' or p != 0:
                        return False
                    p = 1
                if len(st) == 0 or st[-1] != 'a':
                    return False
                st.pop()
        if len(st) != 0:
            return False
        return True

if __name__ == '__main__':
    print(Solution().isValid("abc"))
