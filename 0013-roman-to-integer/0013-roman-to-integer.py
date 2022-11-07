class Solution:
    def romanToInt(self, s: str) -> int:
        dt = { "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900 }
        
        answer = 0
        i = 0
        while i < len(s):
            c = s[i]
            if c in ("I", "X", "C") and i < len(s)-1:
                cc = s[i]+s[i+1]
                if cc in dt:
                    answer += dt[cc]
                    i += 1
                else:
                    answer += dt[c]
            else:
                answer += dt[c]
            
            i += 1
        
        return answer