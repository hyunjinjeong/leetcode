class Solution:
    def isPathCrossing(self, path: str) -> bool:
        # crossing 여부를 봐야 하는구나 ㅋㅋ 원점으로 돌아오는 건줄
        # visited set을 관리하면 되긴 할텐데... 이게 맞을라나? easy라서 맞을 수도?

        x, y = 0, 0

        visited = set()
        visited.add((x, y))

        for c in path:
            if c == "N":
                y += 1 
            elif c == "S":
                y -= 1
            elif c == "E":
                x += 1
            else:
                x -= 1
            
            if (x, y) in visited:
                return True
            
            visited.add((x, y))
        
        return False