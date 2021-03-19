class Solution:
    def canVisitAllRooms(self, rooms):
        n = len(rooms)
        s = [False] * n
        s[0] = True
        q = [0]
        h = 0
        while h < len(q):
            for room in rooms[q[h]]:
                if not s[room]:
                    q.append(room)
                    s[room] = True
            h += 1

        return all(s)
