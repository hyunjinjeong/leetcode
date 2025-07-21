class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        # 결정해야 할 사항은 alice가 어딜 향해 갈 것인가?
        # bob은 항상 0으로 움직이기 떄문에 경로가 정해져 있음
        # bob이 먼저 움직인 경로를 따라가면 alice가 얻을 점수를 잃음
        # 근데.. 최적해를 수식으로 구하지는 못할 것 같음. 즉 다 돌고 나서 max를 찾아야 하지 않을까?
        # BFS를 돌리면서, 턴이 지날 때마다 bob 경로를 따라 노드의 값을 바꿔야 할 듯.
        def find_bob_path(node, path, visited):
            if node == 0:
                self.bob_path = path[:]
                return
            
            visited.add(node)
            for next_node in graph[node]:
                if next_node not in visited:
                    path.append(next_node)
                    find_bob_path(next_node, path, visited)
                    path.pop()

            visited.remove(node)

        # 그래프 만들고
        graph = {i: [] for i in range(len(edges) + 1)}
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)
        
        # alice
        q = collections.deque([(0, amount[0])])
        visited = set([0])
        
        # bob 설정
        self.bob_path = []
        find_bob_path(bob, [bob], set())
        amount[bob] = 0
        bob_index = 1

        max_income = float("-inf")
        while q:
            # 일단 bob을 먼저 한칸씩 돌려야겠지?
            if bob_index < len(self.bob_path):
                bob_node = self.bob_path[bob_index]
                if len(self.bob_path) % 2 == 1 and bob_index == len(self.bob_path) // 2:
                    amount[bob_node] //= 2
                else:
                    amount[bob_node] = 0
                bob_index += 1

            for _ in range(len(q)):
                node, curr_income = q.popleft()
                is_leaf = True

                for next_node in graph[node]:
                    if next_node not in visited:
                        is_leaf = False
                        q.append((next_node, curr_income + amount[next_node]))
                        visited.add(next_node)
                
                if is_leaf:
                    max_income = max(max_income, curr_income)

        return max_income
