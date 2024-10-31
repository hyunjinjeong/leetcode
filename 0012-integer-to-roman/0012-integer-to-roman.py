class Solution:
    def intToRoman(self, num: int) -> str:
        # 큰 수부터 돌리면 되지 않을까?
        roman = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
        ]

        i = 0
        res = []
        while num:
            value, symbol = roman[i]
            count, num = divmod(num, value)
            res.append(symbol * count)
            i += 1
        
        return "".join(res)