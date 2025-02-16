class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        # # k * k 매트릭스에 k개가 들어 있어야 함. 즉 해당 숫자를 제외한 row, col의 모든 값은 0.
        # # conditions 로 그래프를 만들 수 있나? 왜냐면 위상 정렬이랑 비슷한 느낌임
        # # [1, 2], [3 ,2]면 row는 1->2, 3->2. 즉 2보다 1과 3이 앞에 나와야 함. 1과 3은 관계 없고.
        # # [2, 1], [3, 2]면 col은 2->1, 3->2. 3->2->1. 3이 가장 먼저, 다음엔 2, 다음엔 1이 나와야 함.
        # # row랑 col 사이에도 의존성이 있나? 없는 것 같음.
        # # 사이클이 있으면 []고...
        # # 그 다음에 build하는 방법은? 하나를 미리 계산해두자.
        # col_graph = {i: [] for i in range(1, k + 1)}
        # col_in_degrees = {i: 0 for i in range(1, k + 1)}
        # for src, dst in colConditions:
        #     col_graph[src].append(dst)
        #     col_in_degrees[dst] += 1
        
        # # col은 순서를 미리 계산.
        # col_queue = collections.deque()
        # for num, in_degree in col_in_degrees.items():
        #     if in_degree == 0:
        #         col_queue.append(num)
        
        # col_index = 0
        # col_positions = {}
        # while col_queue:
        #     num = col_queue.popleft()
        #     col_positions[num] = col_index
        #     col_index += 1

        #     for next_num in col_graph[num]:
        #         col_in_degrees[next_num] -= 1
        #         if col_in_degrees[next_num] == 0:
        #             col_queue.append(next_num)
        
        # if len(col_positions) != k: # cycle
        #     return []

        # row_graph = {i: [] for i in range(1, k + 1)}
        # row_in_degrees = {i: 0 for i in range(1, k + 1)}
        # for src, dst in rowConditions:
        #     row_graph[src].append(dst)
        #     row_in_degrees[dst] += 1

        # # 다음엔 row를 가지고 실제 위치 계산 
        # row_queue = collections.deque()
        # for num, in_degree in row_in_degrees.items():
        #     if in_degree == 0:
        #         row_queue.append(num)
        
        # res = []
        # while row_queue:
        #     num = row_queue.popleft()
        #     curr = [0] * k
        #     col = col_positions[num]
        #     curr[col] = num
        #     res.append(curr)

        #     for next_num in row_graph[num]:
        #         row_in_degrees[next_num] -= 1
        #         if row_in_degrees[next_num] == 0:
        #             row_queue.append(next_num)
        
        # if len(res) != k: # cycle
        #     return []

        # return res

        # 리팩토링!
        def topological_sort(edges):
            graph = {i: [] for i in range(1, k + 1)}
            in_degree = {i: 0 for i in range(1, k + 1)}

            for src, dst in edges:
                graph[src].append(dst)
                in_degree[dst] += 1

            q = collections.deque()
            for num, degree in in_degree.items():
                if degree == 0:
                    q.append(num)
            
            order = {}
            index = 0
            while q:
                num = q.popleft()
                order[num] = index
                index += 1

                for next_num in graph[num]:
                    in_degree[next_num] -= 1
                    if in_degree[next_num] == 0:
                        q.append(next_num)
            
            if len(order) != k:
                return [] # cycle
            
            return order
        
        order_rows = topological_sort(rowConditions)
        order_cols = topological_sort(colConditions)

        if not (order_rows and order_cols):
            return []
        
        res = [[0] * k for _ in range(k)]
        for i in range(1, k + 1):
            res[order_rows[i]][order_cols[i]] = i

        return res