class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # operation은 거리를 의미함. 즉 j번째 박스에서 i번째 박스로 옮기려면 j - i (nums[j] == 1일 때만)
        # 그냥 각각 루프 돌면서 구하면 될 듯? 그럼 개별은 O(N)이고 총 O(N^2)
        res = [0] * len(boxes)

        for i in range(len(boxes)):
            ops = 0
            
            for j in range(len(boxes)):
                if i == j or boxes[j] == "0":
                    continue
                ops += abs(i - j)
            
            res[i] = ops

        return res
