class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:

        def get_digit_count(num):
            res = 0
            while num:
                num //= 10
                res += 1
            return res
        
        def generate(digit_count, first_digit):
            num = 0

            curr_count, curr_digit = 0, first_digit
            while curr_count < digit_count and curr_digit < 10:
                num = num * 10 + curr_digit

                curr_count += 1
                curr_digit += 1

            return num if get_digit_count(num) == digit_count else -1

        res = []

        low_digit_count, high_digit_count = get_digit_count(low), get_digit_count(high)
        for digit_count in range(low_digit_count, high_digit_count + 1):
            for first_digit in range(1, 10):
                num = generate(digit_count, first_digit)
                if low <= num <= high:
                    res.append(num)
        
        return res