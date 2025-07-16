class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        # 일단 90도로 돌리고 떨구면 되지 않을까
        # 밀고 돌리는게 편할 듯
        m, n = len(boxGrid), len(boxGrid[0])

        # 어케 밀지? greedy가 될 것 같다
        # row 단위로 왼쪽부터 오른쪽으로 돌면서 돌 갯수를 세다가
        # 장애물을 만나면 장애물 왼쪽까지 갱신.
        for row in range(m):
            stones = 0
            last_obstacle = -1
            for col in range(n):
                cell = boxGrid[row][col]
                if cell == "#":
                    stones += 1
                elif cell == "*":
                    for col2 in range(col - 1, last_obstacle, -1):
                        if stones > 0:
                            boxGrid[row][col2] = "#"
                            stones -= 1
                        else:
                            boxGrid[row][col2] = "."
                    last_obstacle = col
            
            for col2 in range(n - 1, last_obstacle, -1):
                if stones > 0:
                    boxGrid[row][col2] = "#"
                    stones -= 1
                else:
                    boxGrid[row][col2] = "."

        # 돌리기
        rotated_box = [[""] * m for _ in range(n)]
        for row in range(n):
            for col in range(m):
                rotated_box[row][col] = boxGrid[m - 1 - col][row]

        return rotated_box
