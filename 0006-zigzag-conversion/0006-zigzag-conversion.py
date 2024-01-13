class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        # 규칙이 있으려나? 그냥 시뮬레이션 해보자.
        ans = [[] for _ in range(numRows)]

        # 일단 numRows만큼 세로로 내려가고
        # 그다음 row==0이 될 때까지 세로로 올라감.. 
        # 다시 내려가고.. 반복

        i = 0
        while i < len(s):
            for row in range(numRows - 1):
                ans[row].append(s[i])
                i += 1
                if i == len(s):
                    break
            
            if i == len(s):
                    break
            
            for row in range(numRows - 1, 0, -1):
                ans[row].append(s[i])
                i += 1
                if i == len(s):
                    break
        
        ans_s = ""
        for r in ans:
            ans_s += "".join(r)
        return ans_s