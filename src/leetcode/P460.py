from collections import OrderedDict, defaultdict


class LFUCache:

    def __init__(self, capacity: int):
        self.d = defaultdict(lambda: OrderedDict())
        self.f = {}
        self.c = capacity
        self.mf = -1

    def get(self, key: int) -> int:
        f = self.f
        d = self.d
        if key in f:
            ff = f[key]
            v = d[ff][key]
            del d[ff][key]
            if not d[ff] and self.mf == ff:
                self.mf = ff + 1
            ff += 1
            f[key] = ff
            d[ff][key] = v
            return v
        return -1

    def put(self, key: int, value: int) -> None:
        c, d, f, mf = self.c, self.d, self.f, self.mf
        if key not in f:
            if len(f) == c:
                if mf == -1:
                    if len(f) == 0:
                        return
                    mf = min(f.values())
                k, _ = d[mf].popitem(last=False)
                del f[k]
            f[key] = 0
            mf = 1
        self.mf = mf
        ff = f[key]
        if ff > 0:
            del d[ff][key]
            if not d[ff] and self.mf == ff:
                self.mf = ff + 1
        f[key] += 1
        d[ff + 1][key] = value


if __name__ == '__main__':
    lfu = LFUCache(1)
    lfu.put(2, 1)
    lfu.get(2)
    lfu.put(3, 2)
    lfu.get(2)
    lfu.get(3)
