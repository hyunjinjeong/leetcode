class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        # 일단 steps 중 key를 누르는 건 len(key)이고
        # 결국 몇 번 돌리는지가 중요함.
        # 오른쪽으로 돌리거나 왼쪽으로 돌리거나
        # 딱 바로 생각나는건 DP인데, 경우의 수가 너무 많지 않나?
        # 그래프로 생각해보면? 서로 이어진 캐릭터는 양방향 edge로 이어진 vertex... 어떻게 풀어야 할지 감이 안오고
        
        # 돌린다는 행위는 결국 i = 0에서 시작해서, i += 1하면 오른쪽 rotate, i -= 1하면 왼쪽 rotate임
        # 0에서 i -= 1 하면 len(ring) - 1로 돌아가고.

        def next_i(i, direction):
            if i == 0 and direction == "L":
                return len(ring) - 1
            if i == len(ring) - 1 and direction == "R":
                return 0
            
            if direction == "L":
                return i - 1
            else:
                return i + 1

        def rotate(i, target, direction):
            steps = 0

            while ring[i] != target:
                i = next_i(i, direction)
                steps += 1
            
            return (i, steps)
        
        @cache
        def dfs(i, j):
            if j == len(key):
                return 0

            if ring[i] == key[j]:
                return 1 + dfs(i, j + 1) # click
            else:
                # 이런 느낌?
                left_i, left_steps = rotate(i, key[j], "L")
                right_i, right_steps = rotate(i, key[j], "R")
                left = left_steps + 1 + dfs(left_i, j + 1)
                right = right_steps + 1 + dfs(right_i, j + 1)
                return min(left, right)
        
        return dfs(0, 0)