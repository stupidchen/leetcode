class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [['#', 0]]
        for c in s:
            if stack[-1][0] == c:
                stack[-1][1] += 1
            else:
                stack.append([c, 1])
            while stack[-1][1] >= k:
                stack.pop()
        ret = ''
        for p in stack[1:]:
            ret += p[0] * p[1]
        return ret


if __name__ == '__main__':
    print(Solution().removeDuplicates('deeedbbcccbdaa', 3))
