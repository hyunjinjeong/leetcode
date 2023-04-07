class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # 이걸 계속 돌면서 시뮬레이션할 수는 없을 테니까...
        # 양수면 자기보다 오른쪽에 있는 소행성 중 size가 같거나 큰 게 있으면 없어지고
        # 음수는 반대로 자기보다 왼쪽.
        # stack을 쓴다라...
        
        ans = []
        for asteroid in asteroids:
            if asteroid > 0:
                ans.append(asteroid)
            else:
                has_exploded = False
                while ans and ans[-1] > 0:
                    prev = ans[-1]
                    curr = -1 * asteroid
                    if prev > curr:
                        has_exploded = True
                        break
                    elif prev < curr:
                        ans.pop()
                    else:
                        has_exploded = True
                        ans.pop()
                        break
                
                if not has_exploded:
                    ans.append(asteroid)       
        
        return ans