class Solution:
    def minimumSteps(self, s: str) -> int:
        # 뭔가 규칙이 있나? 그냥 bubble sort 해서 수행 횟수를 세면 되지 않을까
        # 위 방법은 TLE가 뜸. 맞긴 맞네.
        # 오른쪽에서부터 시작해서 가장 마지막 1 index를 저장하고 길이만큼을 더하면 되려나?
        count = 0
        last_one_index = len(s) - 1

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "1":
                count += last_one_index - i
                last_one_index -= 1
        
        return count
