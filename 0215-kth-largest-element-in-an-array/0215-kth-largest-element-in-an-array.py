class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Heap 이용하면 O(nlogk)으로 해결 가능하지만..
        # O(n)으로 가능한 quickselect를 구현해보자.
        left, right = 0, len(nums) - 1
        while True:
            pivot_index = self.partition(nums, left, right)
            if pivot_index == k - 1: # zero-based index라 k-1
                return nums[pivot_index]
            
            if pivot_index < k - 1: # pivot보다 큰 원소가 k개보다 적은 경우. 즉 답이 오른쪽 그룹(pivot보다 작은)에 있음.
                left = pivot_index + 1
            else: # 반대로 답이 왼쪽 그룹(pivot보다 큰)에 있는 경우.
                right = pivot_index - 1

    def partition(self, nums, left, right):
        pivot = random.randint(left, right) # 무작위로 선택
        nums[right], nums[pivot] = nums[pivot], nums[right] # swap 편하도록 맨 뒤로

        pivot_num = nums[right]
        for i in range(left, right+1):
            if nums[i] >= pivot_num: # 문제 조건이 kth largest니까 pivot과 같거나 큰 원소를 왼쪽으로 보냄
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
            
        # 이 시점에서 left는 pivot보다 작은 첫 번째 원소 위치 (swap 후 +1 되므로)
        # 따라서 -1을 해야 pivot의 위치가 됨
        return left - 1