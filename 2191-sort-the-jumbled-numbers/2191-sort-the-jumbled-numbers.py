class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        # 그냥 brute force로 해도 될라나?
        mapped_nums = []
        for i, num in enumerate(nums):
            if num == 0:
                mapped_num = mapping[num]
            else:
                mapped_num = 0
                
                digits = 1
                while num:
                    mapped_num += mapping[num % 10] * digits
                    num //= 10
                    digits *= 10
            
            mapped_nums.append((mapped_num, i))
        
        mapped_nums.sort()
        return [nums[i] for _, i in mapped_nums]
