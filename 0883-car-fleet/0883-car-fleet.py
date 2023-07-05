class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # monotonic increasing stack...
        stack = []
        # position 순으로 정렬한 뒤, 뒤에서부터 남은 시간을 계산하면
        # 뒤에 나온 친구(position이 낮으면)가 time이 더 큰 경우에만 append.
        # 더 낮으면 합쳐져서 fleet이 된 거니까...
        for pos, v in sorted(zip(position, speed), reverse=True):
            dist = target - pos
            time = dist / v 
            
            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)