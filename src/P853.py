class Car:
    def __init__(self, position, speed):
        self.position = position
        self.speed = speed


class Solution:
    def carFleet(self, target, position, speed):
        n = len(position)
        if n == 0:
            return 0
        car = []
        for i in range(n):
            car.append(Car(position[i], speed[i]))
        car = sorted(car, key=lambda c: c.position)
        f = (target - car[n - 1].position) / car[n - 1].speed
        ret = 1
        for i in reversed(range(n - 1)):
            t = (target - car[i].position) / car[i].speed
            if t > f:
                f = t
                ret += 1
        return ret


if __name__ == '__main__':
    s = Solution()
    print(s.carFleet(12, position = [10,8,0,5,3], speed = [2,4,1,1,3]))
