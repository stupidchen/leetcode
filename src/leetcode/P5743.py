class Solution:
    def memLeak(self, memory1: int, memory2: int):
        i = 1
        while max(memory1, memory2) >= i:
            if memory1 == max(memory1, memory2):
                memory1 -= i
            else:
                memory2 -= i
            i += 1
        return [i, memory1, memory2]


if __name__ == '__main__':
    print(Solution().memLeak(2 ** 31, 2 ** 31))
