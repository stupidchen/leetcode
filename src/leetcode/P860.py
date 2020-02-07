class Solution:
    def lemonadeChange(self, bills):
        hand5 = 0
        hand10 = 0
        hand20 = 0
        for i in range(len(bills)):
            t = bills[i] - 5
            if hand5 * 5 + hand10 * 10 + hand20 * 20 < t:
                return False
            t20 = t // 20
            if hand20 >= t20:
                t %= 20
                hand20 -= t20
            else:
                t -= hand20 * 20
                hand20 = 0
            t10 = t // 10
            if hand10 >= t10:
                t %= 10
                hand10 -= t10
            else:
                t -= hand10 * 10
                hand10 = 0
            t5 = t // 5
            if hand5 >= t5:
                t %= 5
                hand5 -= t5
            else:
                t -= hand5 * 5
                hand5 = 0
            if t != 0:
                return False
            if bills[i] == 20:
                hand20 += 1
            elif bills[i] == 10:
                hand10 += 1
            else:
                hand5 += 1
        return True
