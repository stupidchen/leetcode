class Solution:
    def numOfSubarrays(self, arr, k, threshold):
        r = 0
        n = len(arr)
        s = 0
        for i in range(n):
            if i - k >= 0:
                s -= arr[i - k]
            s += arr[i]
            if s / k >= threshold and i >= k - 1:
                r += 1
        return r


# For test only
SI = (([2, 2, 2, 2, 5, 5, 5, 8], 3, 4), ([1, 1, 1, 1, 1], 1, 0), ([11, 13, 17, 23, 29, 31, 7, 5, 2, 3], 3, 5),
      ([7, 7, 7, 7, 7, 7, 7], 7, 7), ([4, 4, 4, 4], 4, 1))
SO = (3, 5, 6, 1, 1)
TM = 'numOfSubarrays'
if __name__ == '__main__':
    from leetcode.PTester import PTester

    PTester(SI, SO, Solution, TM).run()
