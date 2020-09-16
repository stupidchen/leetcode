from data_structure.trie import Trie


class Solution:
    def findMaximumXOR(self, nums):
        t = Trie(False)
        bn = []
        for num in nums:
            b = bin(num)[2:]
            b = '0' * (32 - len(b)) + b
            bn.append(b)
            t.insert(b, True)

        r = 0
        for b in bn:
            node = t.root
            c = 0
            for i in range(32):
                rb = str(1 - int(b[i]))
                if rb in node.next:
                    c += 1 << (31 - i)
                    node = node.next[rb]
                elif b[i] in node.next:
                    node = node.next[b[i]]
                else:
                    break
            r = max(c, r)
        return r


if __name__ == '__main__':
    print(Solution().findMaximumXOR([3, 10, 5, 25, 2, 8]))
