class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # x / y = A. x = Ay
        # y / z = B. y = Bz
        # x / z = C. x = Cz = ABz
        # 그래프로 표현하면 되지 않을까? edge 가중치를 다 곱하고.
        # 음 근데 반대 방향으로도 갈 수 있구나...
        # 일단 그래프는 맞는 것 같음.
        graph = collections.defaultdict(list)
        variables = set()

        for i, (a, b) in enumerate(equations):
            graph[a].append((b, values[i]))
            graph[b].append((a, 1 / values[i]))
            variables.add(a)
            variables.add(b)
        
        res = []
        
        for a, b in queries:
            if a not in variables or b not in variables:
                res.append(-1.0)
                continue
            has_appended = False

            visited = set()
            q = collections.deque([(a, 1.0)])
            while q:
                curr, val = q.popleft()
                if curr == b:
                    res.append(val)
                    has_appended = True
                    break
                visited.add(curr)

                for next_var, next_val in graph[curr]:
                    if next_var not in visited:
                        q.append((next_var, val * next_val))
            
            if not has_appended:
                res.append(-1.0)
        
        return res