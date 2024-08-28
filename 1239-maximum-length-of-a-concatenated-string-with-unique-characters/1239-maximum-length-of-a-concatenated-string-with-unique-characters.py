class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # unique한걸 찾아야 하네..
        # N이 최대 16이니까 backtracking으로 전부 다 찾는건가 보다
        # decision tree를 그려보면
        # 0 -> un / iq / ue
        # un -> uniq / unue
        # iq -> ique
        # ue -> 끝
        # uniq -> unique
        # unue -> 끝
        # 요런 식으로..?
        # a b c가 있으면 -> 0, a, ab, ac, abc, b, bc, c 를 다 확인해야 함

        self.res = 0

        def dfs(start, curr):
            s = "".join(curr)
            if len(s) == len(set(s)):
                self.res = max(self.res, len(s))
            
            if start == len(arr):
                return

            for i in range(start, len(arr)):
                curr.append(arr[i])
                dfs(i + 1, curr)
                curr.pop()
        
        dfs(0, [])
        return self.res