class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        # # 오른쪽에서 왼쪽으로 돌면서 monotonic stack 쓰면 될 듯?
        # # 그냥 왼쪽부터 돌고 decreasing stack 만들면 그게 답인 것 같다
        # stack = []
        # for i, h in enumerate(heights):
        #     while stack and heights[stack[-1]] <= h:
        #         stack.pop()
        #     stack.append(i)
        
        # return stack

        # monotonic stack에 매몰됐는데 오른쪽부터 돌면 max_height만 저장해도 되네
        max_height = -1

        res = []
        for i in reversed(range(len(heights))):
            if heights[i] > max_height:
                res.append(i)
                max_height = heights[i]
        
        return res[::-1]
