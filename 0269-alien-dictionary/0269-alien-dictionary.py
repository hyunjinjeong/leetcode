class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # 모르겠다!
        # sol: Where two words are adjacent, we need to look for the first difference between them.
        # 이거 규칙만 발견하면 쉽넹... topological sort임
        edges = []
        for i in range(1, len(words)):
            prev, curr = words[i-1], words[i]
            has_broken = False
            for j in range(min(len(prev), len(curr))):
                # 근데 여기서 길이만 다른건 어떻게 처리하지? e.g. abc, abcd
                # 아무런 관계가 없으니 pass가 맞겠다.
                if prev[j] != curr[j]:
                    edges.append([prev[j], curr[j]])
                    has_broken = True
                    break

            if not has_broken and len(prev) > len(curr): # 엣지 케이스, e.g. "abc", "ab"
                return ""
        
        letters = set(c for word in words for c in word)
        graph = {c: set() for c in letters}
        in_degree = {c: 0 for c in letters}
        
        for u, v in edges:
            if v not in graph[u]: # 중복이 있을 수 있음
                graph[u].add(v)
                in_degree[v] += 1
                
        ans = []
        q = collections.deque()
        for c in in_degree:
            if in_degree[c] == 0:
                q.append(c)
        
        while q:
            c = q.popleft()
            ans.append(c)
            for next_c in graph[c]:
                in_degree[next_c] -= 1
                if in_degree[next_c] == 0:
                    q.append(next_c)
        
        # 사이클 유무
        return "".join(ans) if len(ans) == len(letters) else ""