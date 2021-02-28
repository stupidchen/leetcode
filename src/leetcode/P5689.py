RULE = ['type', 'color', 'name']

class Solution:
    def countMatches(self, items, ruleKey, ruleValue):
        t = 0
        for i in range(len(RULE)):
            if RULE[i] == ruleKey:
                t = i
                break
        r = 0
        for item in items:
            if item[t] == ruleValue:
                r += 1
        return r