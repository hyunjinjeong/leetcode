class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # 투 포인터 같은데..?
        ans = []
        p_counter = collections.defaultdict(int)
        for c in p:
            p_counter[c] += 1
            
        sorted_p = sorted(p)
        
        left = 0
        # right - left == len(p)면 조건에 따라 ans에 넣고
        # left를 증가시키고, left를 p_counter에 하나 증가시키고
        # 그 전에는 right를 p_counter에 하나씩 빼고...
        for right in range(len(s)):
            if s[right] not in p_counter:
                left = right + 1
                continue
            
            if right - left + 1 == len(p):
                curr = s[left:right+1]
                if sorted(curr) == sorted_p:
                    ans.append(left)
                left += 1
        
        return ans