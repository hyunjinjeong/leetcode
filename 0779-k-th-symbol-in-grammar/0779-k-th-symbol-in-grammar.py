class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # 0
        # 0 / 1
        # 01 / 10
        # 0110 / 1001
        # 01101001 / 10010110
        # 0110100110010110 / 1001011001101001
        # 요런 식으로 쭉 늘어남
        # 보니까 이전 row에서 0->1, 1->0으로 뒤집은 값이 붙네
        # 그러면 row를 다 안 구해도 계산할 수 있으려나?
        # (n, k)는 (n-1, k // 2) 인가?
        # 0 / 01 / 0110 일 때
        # (3, 1), (3, 2)는 0에서 나온 거고
        # (3, 3), (3, 4)는 1에서 나온 거임
        # (2, 1), (2, 2)는 모두 (1, 1)에서 나온거.
        # (1, 1)은 0이니까... (2, 1)은 0, (2, 2)는 1
        # 그러면 (n, k)는 (n - 1, k // 2)인데, k % 2가 1이면 이전 값을 뒤집은거, 0이면 이전 값과 같은거.
        # (n, k)부터 시작해서 (1, 1)까지 내려가보면 될 듯?

        def dfs(n, k):
            if n == 1 and k == 1:
                return 0
            
            prev = dfs(n - 1, (k + 1) // 2) # 아 1-indexed임
            if (k + 1) % 2 == 1: # prev가 1이면 0, 0이면 1
                return 1 if prev == 0 else 0
            else:
                return prev
        
        return dfs(n, k)