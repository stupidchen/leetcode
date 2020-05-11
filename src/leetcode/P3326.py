DX = [1, -1, 0, 0]
DY = [0, 0, 1, -1]

class Solution:
    def floodFill(self, image, sr, sc, newColor):
        c = image[sr][sc]
        n = len(image)
        m = len(image[0])

        def solve(x, y):
            image[x][y] = newColor

            for i in range(4):
                tx, ty = x + DX[i], y + DY[i]
                if 0 <= tx < n and 0 <= ty < m and image[tx][ty] == c:
                    solve(tx, ty)

        if image[sr][sc] != newColor:
            solve(sr, sc)
        return image
