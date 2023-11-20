class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        
        i = 1
        while i <= numRows:
            curr = []
            for j in range(i):
                if j in (0, i-1):
                    curr.append(1)
                else:
                    prev = ans[i-2] # i가 1부터 시작해서...
                    curr.append(prev[j-1] + prev[j])
            
            ans.append(curr)
            i += 1
        
        return ans