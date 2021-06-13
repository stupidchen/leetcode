class Solution:
    def maximumRemovals(self, s, p, removable):
        n = len(s)
        m = len(p)
        removed = [False] * n

        def is_sub_sequence():
            i = 0
            for j, c in enumerate(s):
                if removed[j]:
                    continue
                if c == p[i]:
                    i += 1
                if i == m:
                    return True
            return False

        l, r = 0, len(removable)
        ret = 0
        while l <= r:
            mid = (l + r) >> 1
            for k in range(mid):
                removed[removable[k]] = True
            if is_sub_sequence():
                ret = mid
                l = mid + 1
            else:
                r = mid - 1
            for k in range(mid):
                removed[removable[k]] = False
        return ret


if __name__ == '__main__':
    print(Solution().maximumRemovals(s="abcbddddd", p="abcd", removable=[3, 2, 1, 4, 5, 6]))
