class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        # backtracking? 그냥 다 해보는 수밖에 없어 보인다
        # 결과값은 어떻게 계산하지? set의 크기가 unique한 개수임.

        def dfs(start, substrings):
            if start == len(s):
                return len(substrings)
            
            count = 1
            for i in range(start, len(s)):
                substring = s[start:i + 1]
                if substring in substrings:
                    continue
                
                substrings.add(substring)
                count = max(count, dfs(i + 1, substrings))
                substrings.remove(substring)
            
            return count
        
        return dfs(0, set())
