class Solution:
    def punishmentNumber(self, n: int) -> int:
        # 2번째 컨디션이 문젠데
        # n이 최대 1000이니까 제곱수가 1000000. 자릿수가 많지는 않음
        # backtracking으로 하나씩 전부 해봐야 하나?
        def is_valid(start, curr, target, string):
            if start == len(string) and curr == target:
                return True
            
            for i in range(start, len(string)):
                if is_valid(i + 1, curr + int(string[start:i+1]), target, string):
                    return True
            
            return False

        total = 0
        for i in range(1, n + 1):
            if is_valid(0, 0, i, str(i * i)):
                total += i * i
        return total
