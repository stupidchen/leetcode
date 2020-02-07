class Solution:
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        basket = [-1, -1]
        last = [-1, -1]
        count = [0, 0]
        n = len(tree)
        ret = 0
        for i in reversed(range(n)):
            found = -1
            for j in range(2):
                if basket[j] == -1 or basket[j] == tree[i]:
                    found = j
                    break
            if found != -1:
                basket[found] = tree[i]
                count[found] += 1
                last[found] = i
            else:
                t = min(last)
                d = 0
                for j in range(2):
                    if t == last[j]:
                        d = j
                        break
                count[d] = last[1 - d] - last[d]
                basket[1 - d] = tree[i]
                count[1 - d] = 1
                last[1 - d] = i
            if sum(count) > ret:
                ret = sum(count)
        return ret


if __name__ == '__main__':
    print(Solution().totalFruit([3,3,3,1,2,1,1,2,3,3,4]))
