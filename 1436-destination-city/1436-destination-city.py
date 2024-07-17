class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        # topological sort? 도 되겠고
        # 그냥 DFS 돌려서 도착지도 될듯?
        # 아니면 그냥 outgoing path가 0인거 찾으면 되잖아..?
        outgoing_cities = set()
        for u, v in paths:
            outgoing_cities.add(u)
            
        for _, city in paths:
            if city not in outgoing_cities:
                return city