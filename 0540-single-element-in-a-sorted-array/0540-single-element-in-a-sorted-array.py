class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # bit 연산인줄 알았는데 binary search겠다
        # 왼쪽, 오른쪽 둘 다 nums[mid]와 다르면 그게 정답
        # 근데 조건을 어떻게 줄이지.. 이게 1개짜리가 자기 왼쪽에 있는지 오른쪽에 있는지 알아야겠다
        # 그러면 index랑 num으로 계산이 가능할 듯?

        # 1 1 2 2 3 이면 mid의 경우 i 2, num 2
        # 1 2 2 3 3 이면 mid는 i 2, num 2. 대신 왼쪽이 2 오른쪽이 3.
        # 1 2 2 
        # 1 1 2
        # 1 1, 2 2 이렇게 2개씩 나와야 하니까.. 동일한 숫자가 짝수 -> 홀수 순으로 나와야 함. 즉 숫자가 바뀌는 index는 짝수여야 함.
        # 왼쪽에 1개짜리가 있으면 1 2 2 처럼.. 숫자가 바뀌는 index가 홀수가 됨.

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2

            num_left = nums[mid - 1] if mid > 0 else float("-inf")
            num_right = nums[mid + 1] if mid < len(nums) - 1 else float("inf")
            
            if num_left < nums[mid] < num_right:
                return nums[mid]

            # nums[mid]가 pair의 0번쨰일 수도 있고 1번째일 수도 있고..
            if (nums[mid] == nums[mid - 1] and (mid - 1) % 2 == 1
                or nums[mid] == nums[mid + 1] and mid % 2 == 1):
                right = mid
            else:
                left = mid + 1

