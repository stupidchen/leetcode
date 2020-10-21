class Solution:
    def asteroidCollision(self, asteroids):
        ret = asteroids
        found = True
        while found:
            t = []
            found = False
            i = 1
            n = len(ret)
            l = -1
            while i < n:
                if ret[i - 1] > 0 and ret[i] < 0:
                    found = True
                    collided = True
                    l = i
                    if ret[i - 1] + ret[i] > 0:
                        t.append(ret[i - 1])
                    elif ret[i - 1] + ret[i] < 0:
                        t.append(ret[i])
                else:
                    collided = False
                    t.append(ret[i - 1])
                    l = i - 1
                i += 1
                if collided:
                    i += 1
            if l != n - 1:
                t.append(ret[n - 1])
            if found:
                ret = t

        return ret


if __name__ == '__main__':
    print(Solution().asteroidCollision(asteroids=[1, -2, -2, -2]))
    print(Solution().asteroidCollision(asteroids=[5, -5]))
    print(Solution().asteroidCollision(asteroids=[10, -5]))
    print(Solution().asteroidCollision(asteroids=[10, 2, -5]))
    print(Solution().asteroidCollision(asteroids=[-2, 1, -2, -2]))
    print(Solution().asteroidCollision(asteroids=[5, 10, -5]))
