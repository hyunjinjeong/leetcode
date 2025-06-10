class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        # valid parentheses string 문제랑 비슷하게 greedy로 되려나?
        if len(s) % 2 == 1:
            return False
        
        cmax, cmin = 0, 0
        for c, lock in zip(s, locked):
            print(c, lock)
            if lock == "0":
                cmax += 1 # "("로 사용
                cmin -= 1 # ")"로 사용
            else:
                if c == "(":
                    cmax += 1
                    cmin += 1
                else:
                    cmax -= 1
                    cmin -= 1

            if cmax < 0:
                return False
            
            cmin = max(cmin, 0)
        
        return cmin == 0
