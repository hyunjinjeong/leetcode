class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        # 그래프는 만들면 되고...
        # 1. 최대 1개의 outgoing edge, 2. 사이클이 있을 수 있음
        # node i에서 j까지의 거리를 구하는건 edges[i]에서부터 시작해서 타고 타고 가다가 j까지 가면 됨
        # 노드가 N개가 있을 때... 그 N개에 대해서 모두 거리를 구해야 하나?
        # node 1에 대한 거리를 모두 구하고 -> O(n)
        # node 2에 대한 거리를 모두 구해서 -> O(n)
        # N개의 노드마다 각각 max(dist1, dist2)를 적용한 값을 구할 수 있고
        # res는 그 값의 min으로 하면 되지 않을까?
        N = len(edges)

        def get_distances_from_node(node):
            res = [-1] * N
            visited = set()

            curr = node
            distance = 0
            while curr != -1 and curr not in visited:
                res[curr] = distance
                distance += 1
                visited.add(curr)

                curr = edges[curr]
            
            return res
        
        distances_from_node1 = get_distances_from_node(node1)
        distances_from_node2 = get_distances_from_node(node2)
        
        res = -1
        for i in range(N):
            distance_from_node1, distance_from_node2 = distances_from_node1[i], distances_from_node2[i]
            if distance_from_node1 != -1 and distance_from_node2 != -1:
                if res == -1:
                    res = i
                elif max(distance_from_node1, distance_from_node2) < max(distances_from_node1[res], distances_from_node2[res]):
                    res = i
        
        return res