class Solution:
    def largestOddNumber(self, num: str) -> str:
        # 걍 num을 돌면서 홀수가 있으면 가장 오른쪽 인덱스만 계쏙 저장하면 됨
        # 거꾸로 돌면 바로 리턴할 수 있구나
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 == 1:
                return num[:i + 1]
        return ""