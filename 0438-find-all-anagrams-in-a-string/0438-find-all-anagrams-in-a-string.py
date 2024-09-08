class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # 투포인터 같은데
        # counter를 만들어놓고..
        # 오른쪽을 늘리다가 만족하면 정답에 추가하고 왼쪽을 하나 줄이고 다시 하고.. 그런 식으로?
        # 늘리고 줄이는 조건이 애매하네. character별 갯수를 세야 하나
        # 어차피 window 길이는 정해져 있으니까 그걸로 계속 돌리면 되는구나
        if len(s) < len(p):
            return []
        
        res = []
        p_counter, s_counter = collections.defaultdict(int), collections.defaultdict(int)
        for c in p:
            p_counter[c] += 1

        for i in range(len(p) - 1):
            s_counter[s[i]] += 1

        for right in range(len(p) - 1, len(s)):
            s_counter[s[right]] += 1
            
            left = right - len(p) + 1
            if s_counter == p_counter:
                res.append(left)

            s_counter[s[left]] -= 1
            if s_counter[s[left]] <= 0:
                del s_counter[s[left]]
        
        return res