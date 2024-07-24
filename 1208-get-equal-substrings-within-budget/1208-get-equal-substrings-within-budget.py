class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        # dp의 느낌이 강하게 난다
        # 일단 각각 character에 대한 비용은 미리 계산해둘 수 있음
        # 그러면 prefix sum도 사용 가능하려나?
        # O(n^2)으로 brute force는 가능할 듯
        # index = 0에서 시작해서 쭉 돌고, 1에서 시작해서 쭉 돌고... n-1까지 반복
        # 그러면 이거보다 작은 방법이 필요하다. O(nlogn)이나 O(n)
        # two pointer?
        # 쭉쭉 더해가다가.. curr_cost가 maxCost보다 높아지면 left += 1을 하면 되지 않을까
        def get_cost(i):
            return abs(ord(s[i]) - ord(t[i]))

        ans = 0

        curr_cost = 0
        left = 0
        for right in range(len(s)):
            curr_cost += get_cost(right)
            
            if curr_cost > maxCost:
                curr_cost -= get_cost(left)
                left += 1
            else:
                ans = max(right - left + 1, ans)
        
        return ans