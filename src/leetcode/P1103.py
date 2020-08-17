class Solution:
    def distributeCandies(self, candies, num_people):
        r = [0] * num_people
        i = 1
        j = 0
        while candies != 0:
            r[j] += min(i, candies)
            candies -= min(i, candies)
            j = (j + 1) % num_people
            i += 1
        return r
