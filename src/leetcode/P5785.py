class Solution:
    def mergeTriplets(self, triplets, target):
        f = [False] * 3
        for triplet in triplets:
            if triplet[0] <= target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]:
                for i in range(3):
                    if triplet[i] == target[i]:
                        f[i] = True
        return all(f)
