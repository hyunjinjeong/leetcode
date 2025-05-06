class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        # set bit 개수에 따라서 그룹화를 한 다음
        # 정렬을 한 다음에 정렬 이후의 숫자와 기존 숫자가 같은 그룹에 있는지 확인하기?
        def get_set_bits(n):
            count = 0
            while n:
                count += n & 1
                n >>= 1
            return count

        num_to_set_bit = {num: get_set_bits(num) for num in nums}
        
        sorted_nums = sorted(nums)
        for i in range(len(nums)):
            num, sorted_num = nums[i], sorted_nums[i]
            if num_to_set_bit[num] != num_to_set_bit[sorted_num]:
                return False

        return True
