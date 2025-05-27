class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        # # 3의 제곱수들을 구해놓고 큰거부터 빼면서 greedy하게 될 것 같은데
        # # 3^3 = 3 * 3^2 = 3 * 9 이런 식이니까..
        # nums = []
        
        # num = 1
        # while num <= n:
        #     nums.append(num)
        #     num *= 3
        
        # curr = n
        # for i in range(len(nums) - 1, -1, -1):
        #     if nums[i] <= curr:
        #         curr -= nums[i]
            
        #     if curr == 0:
        #         return True
        
        # return False

        power = 0
        while 3 ** power <= n:
            power += 1
        
        while n and power >= 0:
            num = 3 ** power
            if num <= n:
                n -= num
            
            if n == 0:
                return True

            power -= 1
        
        return False
