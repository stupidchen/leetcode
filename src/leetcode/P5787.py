class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int):
        earliest_round = [5]

        def find_earliest(round, orders):
            if round >= earliest_round[0]:
                return

            m = len(orders)
            hm = m >> 1
            match = []
            for i in range(hm):
                x, y = orders[i], orders[m - i - 1]
                if (x == firstPlayer and y == secondPlayer) or (x == secondPlayer and y == firstPlayer):
                    earliest_round[0] = round
                    return

                if firstPlayer != x and firstPlayer != y and secondPlayer != x and secondPlayer != y:
                    match.append((x, y))

            fixed_orders = [firstPlayer, secondPlayer]
            if m & 1 == 1 and orders[hm] != firstPlayer and orders[hm] != secondPlayer:
                fixed_orders.append(orders[hm])

            m = len(match)
            for i in range(1 << m):
                next_orders = [order for order in fixed_orders]
                for j in range(m):
                    if i | (1 << j) == i:
                        next_orders.append(match[j][0])
                    else:
                        next_orders.append(match[j][1])
                next_orders = sorted(next_orders)
                find_earliest(round + 1, next_orders)

        latest_round = [0]

        def find_latest(round, orders):
            latest_round[0] = max(latest_round[0], round)
            if round > latest_round[0] + 2:
                return
            m = len(orders)
            hm = m >> 1
            match = []
            for i in range(hm):
                x, y = orders[i], orders[m - i - 1]
                if (x == firstPlayer and y == secondPlayer) or (x == secondPlayer and y == firstPlayer):
                    return

                if firstPlayer != x and firstPlayer != y and secondPlayer != x and secondPlayer != y:
                    match.append((x, y))

            fixed_orders = [firstPlayer, secondPlayer]
            if m & 1 == 1 and orders[hm] != firstPlayer and orders[hm] != secondPlayer:
                fixed_orders.append(orders[hm])

            m = len(match)
            for i in range(1 << m):
                next_orders = [order for order in fixed_orders]
                for j in range(m):
                    if i | (1 << j) == i:
                        next_orders.append(match[j][0])
                    else:
                        next_orders.append(match[j][1])
                next_orders = sorted(next_orders)
                find_latest(round + 1, next_orders)

        find_earliest(1, [i + 1 for i in range(n)])
        find_latest(1, [i + 1 for i in range(n)])
        return [earliest_round[0], latest_round[0]]


if __name__ == '__main__':
    print(Solution().earliestAndLatest(28, 2, 18))
