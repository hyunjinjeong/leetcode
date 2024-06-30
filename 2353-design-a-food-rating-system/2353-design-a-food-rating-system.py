class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        # food to rating/cuisine은 dict로 관리하면 될 것 같음
        self.food_map = {foods[i]: [cuisines[i], ratings[i]] for i in range(len(foods))}
        self.heaps = collections.defaultdict(list)

        for i in range(len(cuisines)):
            self.heaps[cuisines[i]].append((-ratings[i], foods[i]))
        
        for cuisine in self.heaps:
            heapq.heapify(self.heaps[cuisine])
        
        print(self.heaps)

        # highest는 cuisine별로 heap 생성하기?
        # 근데 rating을 수정할 때.. heap에서 꺼내고 다시 쓰기가 애매하다.
        # 아..! 삭제를 미룰 수 있음.

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, _ = self.food_map[food]
        self.food_map[food][1] = newRating
        
        heapq.heappush(self.heaps[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.heaps[cuisine]
        while heap:
            heap_rating, food_name = heap[0]
            latest_rating = self.food_map[food_name][1]
            if latest_rating == -heap_rating:
                break
            heapq.heappop(heap)
        
        return heap[0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)