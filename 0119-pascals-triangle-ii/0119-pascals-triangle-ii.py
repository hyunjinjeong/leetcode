class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        ans = [1, 1]
        tmp = []
        for row in range(2, rowIndex + 1):
            for i in range(1, len(ans)):
                tmp.append(ans[i] + ans[i-1])
            
            ans = [1] + tmp + [1]
            tmp = []

        return ans
