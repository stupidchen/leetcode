from collections import defaultdict
from typing import List


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        a = defaultdict(lambda: [])
        for i, transaction in enumerate(transactions):
            name, time, amount, city = transaction.split(',')
            a[name].append((name, int(time), int(amount), city, i))

        r = set()
        for name, transaction_list in a.items():
            transaction_list.sort(key=lambda t: t[1])
            for i, transaction0 in enumerate(transaction_list):
                name0, time0, amount0, city0, index0 = transaction0
                if amount0 > 1000:
                    r.add(index0)
                else:
                    for j, transaction1 in enumerate(transaction_list):
                        name1, time1, amount1, city1, index1 = transaction1
                        if abs(time0 - time1) <= 60 and city0 != city1:
                            r.add(index1)
                            r.add(index0)

        return list(map(lambda t: transactions[t], r))


if __name__ == '__main__':
    print(Solution().invalidTransactions(
        ["bob,689,1910,barcelona","alex,696,122,bangkok","bob,832,1726,barcelona","bob,820,596,bangkok","chalicefy,217,669,barcelona","bob,175,221,amsterdam"]))
