class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # dict 사용해서 캐릭터별로 처음 나온 포지션 저장하고
        # 돌면서 지금 캐릭터랑 동일한게 있으면 a-z까지 확인하면서
        # set에다가 저장하면 되지 않으려나?
        # 그러면 시간 O(n) 공간 O(1)에 가능. 알파벳이 26개니까.
        # ans set까지 생각하면... 최대 개수가 26*26이니까 그래도 O(1)인가?
        
        # 방향은 맞았는데... 더 최적화할 수 있었음.
        first, last = {}, {}
        for i, c in enumerate(s):
            if c not in first:
                first[c] = i
            last[c] = i
        
        ans = 0
        for c in "abcdefghijklmnopqrstuvwxyz":
            if c not in first:
                continue
            
            # palindrome이면 특정 문자가 양 사이드, 가운데에 있는 문자 개수만 세면 됨!
            between = set()
            for mid in range(first[c] + 1, last[c]):
                between.add(s[mid])
            
            ans += len(between)
        
        return ans