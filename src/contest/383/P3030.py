from collections import defaultdict
from typing import List

REGION_SIZE = 3


class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        n = len(image)
        m = len(image[0])
        bounded_region = defaultdict(lambda: defaultdict(list))
        for i in range(n - REGION_SIZE + 1):
            for j in range(m - REGION_SIZE + 1):
                intensity = 0
                region_n, region_m = i + REGION_SIZE, j + REGION_SIZE
                is_region = True
                for r in range(i, region_n):
                    for c in range(j, region_m):
                        tr, tc = r + 1, c
                        if tr < region_n and abs(image[tr][tc] - image[r][c]) > threshold:
                            is_region = False
                        tr, tc = r, c + 1
                        if tc < region_m and abs(image[tr][tc] - image[r][c]) > threshold:
                            is_region = False
                        if not is_region:
                            break
                        intensity += image[r][c]
                avg_intensity = intensity // 9
                if is_region:
                    for r in range(i, region_n):
                        for c in range(j, region_m):
                            bounded_region[r][c].append(avg_intensity)
        res = [[0] * m for i in range(n)]
        for i in range(n):
            for j in range(m):
                bounded = bounded_region[i][j]
                if bounded:
                    res[i][j] = sum(bounded_region[i][j]) // len(bounded_region[i][j])
                else:
                    res[i][j] = image[i][j]
        return res


if __name__ == '__main__':
    r = Solution().resultGrid(image=[[5, 6, 7, 10], [8, 9, 10, 10], [11, 12, 13, 10]], threshold=3)
    print(r)
