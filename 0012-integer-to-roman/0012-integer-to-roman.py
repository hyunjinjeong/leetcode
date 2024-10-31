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

        res = []
        for value, symbol in roman:
            count, num = divmod(num, value)
            res.append(symbol * count)
            if num == 0:
                break
        
        return "".join(res)