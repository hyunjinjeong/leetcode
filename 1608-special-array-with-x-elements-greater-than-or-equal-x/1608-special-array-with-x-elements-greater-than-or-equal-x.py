class Solution:
    def specialArray(self, nums: List[int]) -> int:
        # 숫자가 0~1000이니까 다 시도해볼 순 있는데... 더 최적화할 수 있지 않을까
        # 일단 brute force로

        for x in range(max(nums) + 1):
            cnt = 0
            broken = False
            for num in nums:
                if num >= x:
                    cnt += 1
                if cnt > x:
                    broken = True
                    break
            if cnt == x and not broken:
                return x
        
        return -1
            