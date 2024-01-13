class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # 그냥 계속 가면서 확인..?은 안되는게 infinite이라 안 끝남
        # hint 1: 포지션을 계산하라?

        x, y = 0, 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d_i = 0

        for ins in instructions:
            if ins == "L":
                d_i = (d_i - 1 + 4) % 4
            elif ins == "R":
                d_i = (d_i + 1) % 4
            else:
                x += directions[d_i][0]
                y += directions[d_i][1]
        
        # 무한히 반복이니까... 포지션이 바뀌면 무조건 circle이네
        return x == 0 and y == 0 or d_i != 0