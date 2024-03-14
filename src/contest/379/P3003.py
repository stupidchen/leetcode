class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        states = {(0, 0, 0)}  # (partition number, characters, if changed)
        for c in s:
            char = 1 << (ord(c) - ord('a'))
            new_states = set()
            for state in states:
                partitions, chars, if_changed = state
                if bin(chars | char).count('1') <= k:
                    new_states.add((partitions, chars | char, if_changed))
                else:
                    new_states.add((partitions + 1, char, if_changed))

                if if_changed == 0:
                    for i in range(26):
                        char_changed = 1 << i
                        if char_changed != char:
                            if bin(chars | char_changed).count('1') <= k:
                                new_states.add((partitions, chars | char_changed, 1))
                            else:
                                new_states.add((partitions + 1, char_changed, 1))
            states = new_states

        res = max(states)[0] + 1
        return res


if __name__ == '__main__':
    r = Solution().maxPartitionsAfterOperations(s="aabaab", k=3)
    print(r)
