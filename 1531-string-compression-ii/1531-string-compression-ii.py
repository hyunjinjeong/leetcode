class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        # 1개짜리는 숫자가 안 붙음. 그러면 1개 지우면 1개 없어짐
        # 2개 이상부터는 숫자가 붙는다... a2 a3 a4 이런 식. 그러면 자릿수가 변하거나 모두 지우지 않는 이상 숫자가 변하지 않음.
        # 즉 a4 -> a2는 똑같고... a13 -> a10도 똑같고. 대신 a10 -> a9나, a4 -> '' 은 변함
        # 가성비로 보면 1개짜리를 지우면 무조건 1개가 없어지니 좋고
        # 그 다음엔? 10으로 % 연산한 다음에 remainder가 작은 순서대로 remainder만큼 삭제.
        # a2면 2개... 그럼 2개 없어짐. 아.. 근데 a10이면 1개 줄이면 a9, a12면 3개 줄여야 a9.
        # 그러면 10보다 크면 remainder + 1개만큼 삭제해야 줄어듦.
        # 흠 근데 지우다가 붙어버리는 경우가 있음. 그럼 이런 식으로 매뉴얼하게는 못하겠다
        # 생각나는건 DP인데...
        
        @cache
        def dfs(i, char, count, k):
            if k < 0:
                return 100
            if i == len(s):
                return 0
            
            delete_char = dfs(i + 1, char, count, k - 1)
            if s[i] == char:
                keep_char = dfs(i + 1, char, count + 1, k) + (1 if count in (1, 9, 99) else 0)
            else:
                keep_char = dfs(i + 1, s[i], 1, k) + 1
            
            return min(delete_char, keep_char)
        
        return dfs(0, "", 0, k)