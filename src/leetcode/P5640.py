from data_structure.trie import Trie

BIT = 32


class Solution:
    def maximizeXor(self, nums, queries):
        t = Trie()
        nums = sorted(nums)

        def find(node, bit, result, x):
            ret = -1
            if node.val:
                ret = result

            if bit < 0:
                return ret

            b = 1 << bit
            k = x & b
            if k > 0:
                if '0' in node.next:
                    ret = max(ret, find(node.next['0'], bit - 1, result + b, x))
                elif '1' in node.next:
                    ret = max(ret, find(node.next['1'], bit - 1, result, x))
            else:
                if '1' in node.next:
                    ret = max(ret, find(node.next['1'], bit - 1, result + b, x))
                elif '0' in node.next:
                    ret = max(ret, find(node.next['0'], bit - 1, result, x))

            return ret

        queries = sorted([(query[1], query[0], i) for (i, query) in enumerate(queries)])
        r = [-1] * len(queries)
        i = 0
        for query in queries:
            while i < len(nums) and nums[i] <= query[0]:
                p = ''
                num = nums[i]
                for j in range(BIT):
                    if (num | (1 << j)) == num:
                        p = '1' + p
                    else:
                        p = '0' + p
                t.insert(p, True)
                i += 1
            r[query[2]] = find(t.root, BIT - 1, 0, query[1])
        return r


if __name__ == '__main__':
    print(Solution().maximizeXor(nums=[5, 2, 4, 6, 6, 3], queries=[[12, 4], [8, 1], [6, 3]]))
    print(Solution().maximizeXor(nums=[0, 1, 2, 3, 4], queries=[[3, 1], [1, 3], [5, 6]]))
