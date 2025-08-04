class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # # operation은 거리를 의미함. 즉 j번째 박스에서 i번째 박스로 옮기려면 j - i (nums[j] == 1일 때만)
        # # 그냥 각각 루프 돌면서 구하면 될 듯? 그럼 개별은 O(N)이고 총 O(N^2)
        # res = [0] * len(boxes)

        # for i in range(len(boxes)):
        #     ops = 0
            
        #     for j in range(len(boxes)):
        #         if i == j or boxes[j] == "0":
        #             continue
        #         ops += abs(i - j)
            
        #     res[i] = ops

        # return res

        # 통과는 하는데 더 최적화가 필요하구나
        # 001011 이면
        # 0 -> / (2 - 0) + (4 - 0) + (5 - 0)
        # 1 -> / (2 - 1) + (4 - 1) + (5 - 1)
        # 2 -> / (4 - 2) + (5 - 2)
        # 3 -> (3 - 2) / (4 - 3) + (5 - 3)
        # 4 -> (4 - 2) + / (5 - 4)
        # 5 -> / (5 - 2) + (5 - 4)
        # 왼쪽 오른쪽 나눠서 구하면 될 듯?
        N = len(boxes)

        res = [0] * N

        balls, moves = 0, 0
        for i in range(N):
            res[i] += balls + moves
            moves += balls
            balls += int(boxes[i])

        balls, moves = 0, 0
        for i in reversed(range(N)):
            res[i] += balls + moves
            moves += balls
            balls += int(boxes[i])

        return res
