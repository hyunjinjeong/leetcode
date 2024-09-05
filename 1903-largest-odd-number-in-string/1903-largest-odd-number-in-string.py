class Solution:
    def largestOddNumber(self, num: str) -> str:
        # 걍 num을 돌면서 홀수가 있으면 가장 오른쪽 인덱스만 계쏙 저장하면 됨
        right = -1
        for i in range(len(num)):
            c = num[i]
            if int(c) % 2 == 1:
                right = i
        
        return num[:right+1] if right > -1 else ""