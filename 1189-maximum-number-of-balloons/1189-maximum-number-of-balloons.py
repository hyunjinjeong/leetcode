class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # 그냥 숫자만 세면 되는거 아닌가..? b a ll oo n. l이랑 o는 2개씩 들어가네..
        counter = collections.defaultdict(int)

        for c in text:
            if c in "balon":
                counter[c] += 1
        
        ans = float("inf")
        for c in "ban":
            ans = min(counter[c], ans)
        for c in "lo":
            ans = min(counter[c] // 2, ans)
        
        return ans