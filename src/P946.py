class Solution:
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []
        j = 0
        for i in pushed:
            stack.append(i)
            while len(stack) > 0 and stack[-1] == popped[j]:
                stack = stack[:-1]
                j += 1
        return j == len(pushed)

if __name__ == '__main__':
    print(Solution().validateStackSequences([1, 2, 3, 4 ,5], [4, 3, 5, 1, 2]))
