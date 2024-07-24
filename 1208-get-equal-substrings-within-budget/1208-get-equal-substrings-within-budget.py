class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        # dp의 느낌이 강하게 난다
        # 일단 각각 character에 대한 비용은 미리 계산해둘 수 있음
        # 그러면 prefix sum도 사용 가능하려나?
        # O(n^2)으로 brute force는 가능할 듯
        # index = 0에서 시작해서 쭉 돌고, 1에서 시작해서 쭉 돌고... n-1까지 반복
        # 그러면 이거보다 작은 방법이 필요하다. O(nlogn)이나 O(n)
        N = len(s)

        ans = 0

        for i in range(N):
            curr_length, curr_cost = 0, 0
            for j in range(i, N):
                cost = abs(ord(s[j]) - ord(t[j]))
                if curr_cost + cost > maxCost:
                    break    
                
                curr_length += 1
                curr_cost += cost
            
            ans = max(curr_length, ans)
            
        return ans