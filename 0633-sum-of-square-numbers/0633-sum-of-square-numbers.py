class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # c까지 제곱해서 나오는 수를 저장하고 숫자를 돌면서 c - num^2가 있는지 확인하면 된다.
        square_nums = set()
        
        num = 0
        while num * num <= c:
            square_num = num * num
            square_nums.add(square_num)
            if c - square_num in square_nums:
                return True
            num += 1

        return False
