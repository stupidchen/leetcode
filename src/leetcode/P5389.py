from collections import defaultdict


class Solution:
    def displayTable(self, orders):
        d = defaultdict(lambda: defaultdict(lambda: 0))
        fs = set()
        for order in orders:
            c, t, f = order
            d[t][f] += 1
            fs.add(f)

        fs = sorted(fs)
        ts = sorted(d.keys(), key=lambda x: int(x))
        r = [['Table'] + fs]
        for t in ts:
            r.append([t])
            for f in fs:
                r[-1].append(str(d[t][f]))
        return r


if __name__ == '__main__':
    print(Solution().displayTable(
        [["Laura","2","Bean Burrito"],["Jhon","2","Beef Burrito"],["Melissa","2","Soda"]]))
