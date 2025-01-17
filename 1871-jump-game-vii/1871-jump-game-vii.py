class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        # 그러니까 i보다 오른쪽에 있는 것 중 minJump ~ maxJump 사이의 구간에 0인 친구로만 점프가 가능하다 이거구만
        if s[-1] == "1":
            return False

        # BFS로 가능
        visited = set()
        q = collections.deque([0])
        max_index = 0 # 요게 중요한 트릭이었네... 
        
        while q:
            i = q.popleft()
            for j in range(max(max_index + 1, i + minJump), min(i + maxJump + 1, len(s))):
                if s[j] == "0":
                    q.append(j)
                    if j == len(s) - 1:
                        return True
                max_index = j
            # max_index = i + maxJump
        
        return False