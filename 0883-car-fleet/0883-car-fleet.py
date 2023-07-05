class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # monotonic increasing stack... 과 비슷한 개념
        ans = 0
        last_time = -1
        # position 순으로 정렬한 뒤, 뒤에서부터 남은 시간을 계산하면
        # 뒤에 나온 친구(position이 낮으면)가 time이 더 큰 경우에만 더하기.
        # 더 낮으면 합쳐져서 fleet이 된 거니까...
        for pos, v in sorted(zip(position, speed), reverse=True):
            dist = target - pos
            time = dist / v 
            
            if time > last_time:
                ans += 1
                last_time = time

        return ans