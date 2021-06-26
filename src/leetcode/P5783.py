import heapq
from collections import defaultdict


class MovieRentingSystem:

    def __init__(self, n, entries):
        movies_in_shop = defaultdict(lambda: {})
        movies_heap = defaultdict(lambda: [])
        rent_movies = set()
        dirty_rent_movies = set()
        dirty_movies = set()
        rent_movies_heap = []
        for entry in entries:
            shop, movie, price = entry
            movies_in_shop[shop][movie] = price
            heapq.heappush(movies_heap[movie], (price, shop))
        self.movies_heap = movies_heap
        self.rent_movies = rent_movies
        self.rent_movies_heap = rent_movies_heap
        self.dirty_rent_movies = dirty_rent_movies
        self.dirty_movies = dirty_movies
        self.movies_in_shop = movies_in_shop

    def search(self, movie):
        movies_heap = self.movies_heap[movie]
        rent_movies = self.rent_movies
        dirty_movies = self.dirty_movies
        pop_entries = []
        for i in range(5):
            found = False
            while movies_heap:
                price, shop = movies_heap[0]
                heapq.heappop(movies_heap)
                if (shop, movie) in rent_movies:
                    if (shop, movie) in dirty_movies:
                        dirty_movies.remove((shop, movie))
                    continue
                else:
                    pop_entries.append((price, shop))
                    found = True
                    break
            if not found:
                break
        for entry in pop_entries:
            heapq.heappush(movies_heap, entry)
        ret = []
        for entry in pop_entries:
            ret.append(entry[1])
        return ret

    def rent(self, shop, movie):
        price = self.movies_in_shop[shop][movie]
        if (shop, movie) not in self.rent_movies:
            self.rent_movies.add((shop, movie))
            self.dirty_movies.add((shop, movie))
            if (shop, movie) not in self.dirty_rent_movies:
                heapq.heappush(self.rent_movies_heap, (price, shop, movie))

    def drop(self, shop, movie):
        price = self.movies_in_shop[shop][movie]
        if (shop, movie) in self.rent_movies:
            self.rent_movies.remove((shop, movie))
            self.dirty_rent_movies.add((shop, movie))
            if (shop, movie) not in self.dirty_movies:
                heapq.heappush(self.movies_heap[movie], (price, shop))

    def report(self):
        rent_movies_heap = self.rent_movies_heap
        rent_movies = self.rent_movies
        dirty_rent_movies = self.dirty_rent_movies
        pop_entries = []
        for i in range(5):
            found = False
            while rent_movies_heap:
                price, shop, movie = rent_movies_heap[0]
                heapq.heappop(rent_movies_heap)
                if (shop, movie) not in rent_movies:
                    if (shop, movie) in dirty_rent_movies:
                        dirty_rent_movies.remove((shop, movie))
                    continue
                else:
                    pop_entries.append((price, shop, movie))
                    found = True
                    break
            if not found:
                break
        for entry in pop_entries:
            heapq.heappush(rent_movies_heap, entry)
        ret = []
        for entry in pop_entries:
            ret.append([entry[1], entry[2]])
        return ret


if __name__ == '__main__':
    ss = MovieRentingSystem(3, [[0, 1, 5], [0, 2, 6], [0, 3, 7], [1, 1, 4], [1, 2, 7], [2, 1, 5]])
    ss.rent(1, 1)
    print(ss.search(1))
    ss.drop(1, 1)
    ss.rent(1, 1)
    ss.drop(1, 1)
    ss.rent(1, 1)
    ss.rent(0, 1)
    ss.drop(1, 1)
    ss.rent(2, 1)
    ss.drop(2, 1)
    ss.drop(0, 1)
    ss.rent(0, 1)
    ss.rent(2, 1)
    ss.drop(2, 1)
    ss.drop(0, 1)
    print(ss.search(1))
