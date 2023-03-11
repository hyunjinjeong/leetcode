class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        # 초기화. len(p)-1 만큼 채워 놓음. 스페셜 케이스 없애기 위해...
        p_counter = collections.Counter(p)
        curr_counter = collections.Counter(s[:len(p)-1])
        
        for right in range(len(p)-1, len(s)):
            curr_counter[s[right]] += 1
            left = right - len(p) + 1
            if p_counter == curr_counter:
                ans.append(left)
            curr_counter[s[left]] -= 1
            
        return ans