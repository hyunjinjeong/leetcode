class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = 0, 0
        new_nums = []
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                new_nums.append(nums1[i])
                i += 1
            else:
                new_nums.append(nums2[j])
                j += 1
        
        while i < m:
            new_nums.append(nums1[i])
            i += 1
        while j < n:
            new_nums.append(nums2[j])
            j += 1
        
        # 요렇게 하면 O(n) 공간 복잡도인데, O(1)으로 가능하겠지 아마?
        for i in range(m + n):
            nums1[i] = new_nums[i]