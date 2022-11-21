class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        answer = []
        right = 0
        
        # 우선 0 이상인 수가 나타날 때까지 right를 오른쪽으로 옮기고..
        for num in nums:
            if num >= 0:
                break
            right += 1
            
        # left는 끝부터 0, right는 시작부터 len(nums)-1까지 달린다
        left = right - 1
        while left >= 0 and right < len(nums):
            if abs(nums[left]) < abs(nums[right]):
                answer.append(nums[left] ** 2)
                left -= 1
            else:
                answer.append(nums[right] ** 2)
                right += 1
        
        # left 혹은 right 둘 중 하나만 남음. 둘 다 처리
        while left >= 0:
            answer.append(nums[left] ** 2)
            left -= 1
        
        while right < len(nums):
            answer.append(nums[right] ** 2)
            right += 1
        
        return answer
        
        # 요렇게 안하고 queue 사용하는 방법도 있다. 그러면 맨 위에 탐색 단계가 없어진다.
        # left는 0부터 오른쪽으로, right는 끝에서부터 왼쪽으로, 조건은 while left <= right..