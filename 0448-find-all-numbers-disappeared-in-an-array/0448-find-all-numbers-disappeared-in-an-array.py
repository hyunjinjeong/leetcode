class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # 그냥 푸는건 간단한데... follow up을 어떻게 하지?
        # constant면 bit 연산을 사용해야 하나?

        # 간단하게 hashmap. 공간 n 시간 n
        ans = []

        counter = collections.Counter(nums)

        for num in range(1, len(nums) + 1):
            if counter.get(num, 0) == 0:
                ans.append(num)

        return ans