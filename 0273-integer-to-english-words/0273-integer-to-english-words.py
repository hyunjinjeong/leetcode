class Solution:
    def numberToWords(self, num: int) -> str:
        num_to_word = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety",
            100: "Hundred"
        }

        def build_words(n): # n <= 999
            res = []
            if n >= 100:
                res.append(num_to_word[n // 100])
                res.append(num_to_word[100])
                n %= 100
            if n >= 20:
                res.append(num_to_word[(n // 10) * 10])
                n %= (n // 10) * 10
            if n:
                res.append(num_to_word[n])
            
            return " ".join(res)
        
        if num == 0:
            return "Zero"

        res = []
        if num >= 10 ** 9:
            res.append(build_words(num // (10 ** 9)))
            res.append("Billion")
            num %= (10 ** 9)
        if num >= 10 ** 6:
            res.append(build_words(num // (10 ** 6)))
            res.append("Million")
            num %= (10 ** 6)
        if num >= 10 ** 3:
            res.append(build_words(num // (10 ** 3)))
            res.append("Thousand")
            num %= (10 ** 3)
        if num:
            res.append(build_words(num))
        
        return " ".join(res)
