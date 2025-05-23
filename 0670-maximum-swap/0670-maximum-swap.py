class Solution:
    def maximumSwap(self, num: int) -> int:
        # # digits는 최대 9개니까 모든 경우의 수를 체크해보면 될 듯? 9C2.
        # max_num = num
        
        # str_num = list(str(num))
        # for i in range(len(str_num)):
        #     for j in range(i + 1, len(str_num)):
        #         str_num[i], str_num[j] = str_num[j], str_num[i]
        #         max_num = max(max_num, int("".join(str_num)))
        #         str_num[i], str_num[j] = str_num[j], str_num[i]
        
        # return max_num
        
        # O(N) 쏠루션
        num_list = list(str(num))

        max_digit = "0"
        max_index = -1
        swap_i, swap_j = -1, -1

        for i in reversed(range(len(num_list))):
            if num_list[i] > max_digit:
                max_digit = num_list[i]
                max_index = i
            elif num_list[i] < max_digit: # max보다 작은 숫자 중 가장 왼쪽의 숫자를 스왑
                swap_i, swap_j = i, max_index
        
        num_list[swap_i], num_list[swap_j] = num_list[swap_j], num_list[swap_i]
        return int("".join(num_list))

