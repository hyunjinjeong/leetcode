class Solution:
    def maximumSwap(self, num: int) -> int:
        # digits는 최대 9개니까 모든 경우의 수를 체크해보면 될 듯? 9C2.
        max_num = num
        
        str_num = list(str(num))
        for i in range(len(str_num)):
            for j in range(i + 1, len(str_num)):
                str_num[i], str_num[j] = str_num[j], str_num[i]
                max_num = max(max_num, int("".join(str_num)))
                str_num[i], str_num[j] = str_num[j], str_num[i]
        
        return max_num
