class Solution:
    def checkValidString(self, s: str) -> bool:
        # # * 처리를 해야 하는데..
        # # *를 (, ), ""로 각각 나눠서 DFS 돌리기?

        # cache = {}

        # def dfs(i, curr_count):
        #     if curr_count < 0:
        #         return False
        #     if i == len(s):
        #         return curr_count == 0
            
        #     if (i, curr_count) in cache:
        #         return cache[(i, curr_count)]
            
        #     c = s[i]
        #     if c == "(":
        #         ans = dfs(i + 1, curr_count + 1)
        #     elif c == ")":
        #         ans = dfs(i + 1, curr_count - 1)
        #     else:
        #         ans = dfs(i + 1, curr_count + 1) or dfs(i + 1, curr_count - 1) or dfs(i + 1, curr_count)
            
        #     cache[(i, curr_count)] = ans
        #     return ans
        
        # return dfs(0, 0)

        # greedy도 됨!
        cmax, cmin = 0, 0
        for c in s:
            if c == "(":
                cmax += 1
                cmin += 1
            elif c == ")":
                cmax -= 1
                cmin -= 1
            else:
                cmax += 1 # * -> (
                cmin -= 1 # * -> )

            if cmax < 0:
                return False

            cmin = max(cmin, 0) # 음수는 될 수 없음
        
        return cmin == 0
