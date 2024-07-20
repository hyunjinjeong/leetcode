class Solution:
    def minFlips(self, s: str) -> int:
        # alternating -> 101010 // 010101 요런 식이구만
        # type 2 operation의 최솟값....
        # 만약 type 2만 있으면 그냥 101010.. or 010101... 이랑 비교해서 min() 구하면 된다
        N = len(s)
        ans = N

        original_left = 0
        zero_start, one_start = 0, 0
        
        for original_right in range(N * 2):
            left = original_left % N
            right = original_right % N

            if original_right % 2 == 0:
                if s[right] == "1":
                    zero_start += 1
                else:
                    one_start += 1
            else:
                if s[right] == "1":
                    one_start += 1
                else:
                    zero_start += 1
            
            if original_right - original_left + 1 >= N: # move left
                ans = min(one_start, zero_start, ans)
                if original_left % 2 == 0:
                    if s[left] == "1":
                        zero_start -= 1
                    else:
                        one_start -= 1
                else:
                    if s[left] == "1":
                        one_start -= 1
                    else:
                        zero_start -= 1
                original_left += 1

        return ans
