class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # 그냥 푸는건 간단한데... follow up을 어떻게 하지?
        # constant면 bit 연산을 사용해야 하나? -> 딱히 떠오르는게 없음
        # 1은 0번째, 2는 1번째, ... 이렇게 가도록 배열을 수정하면? -> 이건 O(n)에 안 됨

        # -로 마킹하는 방법이 있음 ㄷ
        ans = []

        for num in nums:
            index = abs(num) - 1
            if nums[index] > 0:
                nums[index] *= -1
        
        return [i + 1 for i, num in enumerate(nums) if num > 0]