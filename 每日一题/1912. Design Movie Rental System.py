from sortedcontainers import sortedlist
from collections import defaultdict
from typing import List
import heapq


class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.movies = defaultdict(list)
        self.record = defaultdict(dict)  # 记录电影在商店中是否借出
        self.system = defaultdict(dict)  # 每个电影在商店中的价格
        for shop_id, movie_id, price in entries:
            heapq.heappush(self.movies[movie_id], (price, shop_id))
            self.record[movie_id][shop_id] = False
            self.system[shop_id][movie_id] = price
        self.rent_movies = sortedlist.SortedList()  # 已经借出的电影，按照价格排序

    def search(self, movie: int) -> List[int]:
        items = self.movies[movie][::]
        res = []
        while len(res) != 5 and items:
            price, shop_id = heapq.heappop(items)
            if self.record[movie][shop_id] is False:
                res.append(shop_id)
        return res

    def rent(self, shop: int, movie: int) -> None:
        price = self.system[shop][movie]
        self.rent_movies.add([price, shop, movie])
        self.record[movie][shop] = True

    def drop(self, shop: int, movie: int) -> None:
        self.record[movie][shop] = False
        price = self.system[shop][movie]
        self.rent_movies.remove([price, shop, movie])

    def report(self) -> List[List[int]]:
        res = []
        items = self.rent_movies[::]
        while len(res) != 5 and items:
            price, shop, movie = heapq.heappop(items)
            res.append([shop, movie])
        return res

# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()
