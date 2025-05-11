class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        # 연결된 road가 많은 city에 더 높은 값을 주면 되려나? 그러면 높은 값이 많이 더해지니까
        roads_count_for_city = [0] * n
        for start, end in roads:
            roads_count_for_city[start] += 1
            roads_count_for_city[end] += 1
        
        roads_count_for_city.sort()

        max_importance = 0
        for city, roads_count in enumerate(roads_count_for_city):
            # 1부터 순서대로 주면 되니까 city + 1
            max_importance += roads_count * (city + 1)

        return max_importance
