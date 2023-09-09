class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # 그래프를 생성하는 것은 쉬움
        # 티켓 돌면서 from to 연결해주고..
        # lexical order로 하는 건..? graph 자체를 정렬시켜두면 편한가..
        # 아니면 heap 사용하는 방법도 있을 것 같음. 
        # DFS로 돌면서 가능한 첫번째 리턴하면 그게 정답..?
        # 정렬 + deque 써보자..
        graph = collections.defaultdict(list)
        
        # 그래프 초기화. O(N)
        for _from, _to in tickets:
            graph[_from].append(_to)
        
        # 정렬 + deque. O(N * NlogN)
        for key in graph:
            graph[key].sort()
            graph[key] = collections.deque(graph[key])
        
        self.ans = []
        self.ans_found = False
        self.dfs(["JFK"], graph, tickets)
        return self.ans
    
    def dfs(self, curr_path, graph, tickets):
        if self.ans_found:
            return
        if len(curr_path) == len(tickets) + 1:
            for key in curr_path:
                self.ans.append(key)
            self.ans_found = True
            return

        key = curr_path[-1]
        dests = graph[key]
        for _ in range(len(dests)):
            next_key = dests.popleft()
            curr_path.append(next_key)
            self.dfs(curr_path, graph, tickets)
            curr_path.pop()
            dests.append(next_key)