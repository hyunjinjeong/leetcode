class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # 그래프를 생성하는 것은 쉬움
        # 티켓 돌면서 from to 연결해주고..
        # lexical order로 하는 건..? graph 자체를 정렬시켜두면 편한가..
        # 아니면 heap 사용하는 방법도 있을 것 같음. 
        # DFS로 돌면서 가능한 첫번째 리턴하면 그게 정답..?
        # 정렬 + deque 써보자..
        # => 그냥 stack으로만 풀 수 있었음.
        graph = collections.defaultdict(list)
        
        # 그래프 초기화. O(N)
        for src, dst in tickets:
            graph[src].append(dst)
        
        # 정렬. O(N * NlogN). pop() 연산을 효율적으로 하기 위해 reverse 정렬.
        for src in graph:
            graph[src].sort(reverse=True)
        
        ans = []
        stack = ["JFK"]
        while stack:
            next_src = stack[-1]
            if graph[next_src]: # 여기 핵심 아이디어는 더 이상 갈 곳이 없는 경로는 뒤에 추가 되어야 한다는 점.
                stack.append(graph[next_src].pop())
            else:
                ans.append(stack.pop())
        
        return ans[::-1] # 따라서 마지막 결과를 reverse 함