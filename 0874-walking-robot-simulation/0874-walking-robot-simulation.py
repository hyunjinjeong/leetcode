class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # 이동이랑 회전은 그냥 하면 되는데 obstacle을 어떻게 처리할까
        # k번 실행하면서 obstacle인지 확인해야 하나? 그럼 obstacle은 set에 넣어둬야 할 듯
        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)] # up right down left. clockwise
        
        obstacle_set = set()
        for x, y in obstacles:
            obstacle_set.add((x, y))

        direction_index = 0
        pos = (0, 0)

        max_distance = 0
        for command in commands:
            if command == -1:
                direction_index = (direction_index + 1) % 4
            elif command == -2:
                direction_index = (direction_index + 3) % 4
            else:
                direction = DIRECTIONS[direction_index]
                for step in range(command):
                    new_pos = (pos[0] + direction[0], pos[1] + direction[1])
                    if new_pos in obstacle_set:
                        break
                    pos = new_pos
            
            max_distance = max(max_distance, pos[0]**2 + pos[1]**2)
        
        return max_distance
