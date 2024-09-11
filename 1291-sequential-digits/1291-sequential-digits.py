class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:

        def get_digit_count(num):
            res = 0
            while num:
                num //= 10
                res += 1
            return res

        digits = "123456789"
        res = []
        
        low_digit_count, high_digit_count = get_digit_count(low), get_digit_count(high)
        for digit_count in range(low_digit_count, high_digit_count + 1):
            for first_digit in range(10 - digit_count):
                num = int(digits[first_digit:first_digit + digit_count])
                if low <= num <= high:
                    res.append(num)
        
        return res