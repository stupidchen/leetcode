from typing import List


class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        block = set()
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    block.add((r, c))

        visited = {((0, 0), (0, 1)): 0}
        goal = ((n - 1, n - 2), (n - 1, n - 1))
        q = [((0, 0), (0, 1), 0)]
        h = 0
        while h < len(q):
            tail, head, step = q[h]
            horizontal = tail[0] == head[0]
            if horizontal:
                if head[1] + 1 < n:
                    # move right
                    next_head = (head[0], head[1] + 1)
                    if next_head not in block:
                        next_state = (head, next_head)
                        if next_state not in visited:
                            visited[next_state] = step + 1
                            q.append((head, next_head, step + 1))

                if head[0] + 1 < n and tail[0] + 1 < n:
                    # rotate clockwise
                    if (head[0] + 1, head[1]) not in block and (tail[0] + 1, tail[1]) not in block:
                        next_head = (tail[0] + 1, tail[1])
                        next_state = (tail, next_head)
                        if next_state not in visited:
                            visited[next_state] = step + 1
                            q.append((tail, next_head, step + 1))

                    # move down
                    if (head[0] + 1, head[1]) not in block and (tail[0] + 1, tail[1]) not in block:
                        next_tail = (tail[0] + 1, tail[1])
                        next_head = (head[0] + 1, head[1])
                        next_state = (next_tail, next_head)
                        if next_state not in visited:
                            visited[next_state] = step + 1
                            q.append((next_tail, next_head, step + 1))
            else:
                if head[0] + 1 < n:
                    # move down
                    next_head = (head[0] + 1, head[1])
                    if next_head not in block:
                        next_state = (head, next_head)
                        if next_state not in visited:
                            visited[next_state] = step + 1
                            q.append((head, next_head, step + 1))

                if head[1] + 1 < n and tail[1] + 1 < n:
                    # rotate counterclockwise
                    if (head[0], head[1] + 1) not in block and (tail[0], tail[1] + 1) not in block:
                        next_head = (tail[0], tail[1] + 1)
                        next_state = (tail, next_head)
                        if next_state not in visited:
                            visited[next_state] = step + 1
                            q.append((tail, next_head, step + 1))

                    # move right
                    if (head[0], head[1] + 1) not in block and (tail[0], tail[1] + 1) not in block:
                        next_tail = (tail[0], tail[1] + 1)
                        next_head = (head[0], head[1] + 1)
                        next_state = (next_tail, next_head)
                        if next_state not in visited:
                            visited[next_state] = step + 1
                            q.append((next_tail, next_head, step + 1))
            if goal in visited:
                return visited[goal]
            h += 1
        return -1


if __name__ == '__main__':
    r = Solution().minimumMoves(grid=[[0, 0, 0, 0, 0, 1],
                                      [1, 1, 0, 0, 1, 0],
                                      [0, 0, 0, 0, 1, 1],
                                      [0, 0, 1, 0, 1, 0],
                                      [0, 1, 1, 0, 0, 0],
                                      [0, 1, 1, 0, 0, 0]])
    print(r)
