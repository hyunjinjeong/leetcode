class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # monotonic increasing stack? 도 필요 없네
        # 변수 하나면 될 듯?
        num = -1

        for i in range(len(arr) - 1, -1, -1):
            curr = arr[i]
            
            arr[i] = num
            num = max(curr, num)
                
        return arr