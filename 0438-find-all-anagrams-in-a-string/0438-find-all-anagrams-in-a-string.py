class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        # 초기화. len(p) 만큼은 채워 놓음.
        p_counter = collections.Counter(p)
        curr_counter = collections.Counter(s[:len(p)])
        
        # 스페셜 케이스
        if p_counter == curr_counter:
            ans.append(0)
        
        for right in range(len(p), len(s)):
            curr_counter[s[right - len(p)]] -= 1
            curr_counter[s[right]] += 1
            
            if p_counter == curr_counter:
                ans.append(right - len(p) + 1)
            
        return ans