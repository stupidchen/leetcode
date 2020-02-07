class Solution:
    def sumEvenAfterQueries(self, A: 'List[int]', queries: 'List[List[int]]') -> 'List[int]':
        ret = []
        sum = 0
        for a in A:
            if a & 1 == 0:
                sum += a
        for query in queries:
            v, i = query
            if A[i] & 1 == 0:
                sum -= A[i]
            A[i] += v
            if A[i] & 1 == 0:
                sum += A[i]
            ret.append(sum)
        return ret
