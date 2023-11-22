class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # dict 사용해서 캐릭터별로 처음 나온 포지션 저장하고
        # 돌면서 지금 캐릭터랑 동일한게 있으면 a-z까지 확인하면서
        # set에다가 저장하면 되지 않으려나?
        # 그러면 시간 O(n) 공간 O(1)에 가능. 알파벳이 26개니까.
        # ans set까지 생각하면... 최대 개수가 26*26이니까 그래도 O(1)인가?
        
        pos = {}
        last_pos = {}
        for i in range(2):
            last_pos[s[i]] = i
            if s[i] not in pos:
                pos[s[i]] = i
        
        ans = set()
        for i in range(2, len(s)):
            if s[i] in pos and pos[s[i]] <= i - 2:
                for c in "abcdefghijklmnopqrstuvwxyz":
                    if c in last_pos and last_pos[c] > pos[s[i]]:
                        ans.add(f"{s[i]}{c}{s[i]}")
                
            if s[i] not in pos:
                pos[s[i]] = i
            last_pos[s[i]] = i
        
        return len(ans)