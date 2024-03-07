from collections import defaultdict, Counter


class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        lo = defaultdict(lambda: -1)
        counter = Counter()
        for index, letter in enumerate(s):
            lo[letter] = max(lo[letter], index)
            counter[letter] += 1

        last = max(counter.values())
        survivor = []
        for letter, location in lo.items():
            if counter[letter] == last:
                survivor.append((location, letter))
        survivor.sort()
        return ''.join(map(lambda x: x[1], survivor))

