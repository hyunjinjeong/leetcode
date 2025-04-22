class Solution:
    def minimumLength(self, s: str) -> int:
        # 그냥 3개 있으면 1개로 줄이면 되는거 아님?
        # 3개 이상이면..? 2개씩 줄일 수 있음. 4->2, 5->1, 6->2, 7->1... 짝수면 2개, 홀수면 1개가 된다.
        length = len(s)
        
        counter = collections.Counter(s)
        for c, count in counter.items():
            if count < 3:
                continue
            
            if count % 2:
                length -= (count - 1)
            else:
                length -= (count - 2)
        
        return length
