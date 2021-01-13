class Solution:
    def numRescueBoats(self, people, limit):
        people = sorted(people)
        r = 0
        i, j = 0, len(people) - 1
        while i <= j:
            if people[i] + people[j] > limit:
                j -= 1
                r += 1
            else:
                i += 1
                j -= 1
                r += 1
        return r
