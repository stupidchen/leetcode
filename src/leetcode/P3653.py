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
