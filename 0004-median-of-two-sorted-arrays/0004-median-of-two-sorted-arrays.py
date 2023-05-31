class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            # 항상 num1이 더 짧도록.
            return self.findMedianSortedArrays(nums2, nums1)
        
        total_length = len(nums1) + len(nums2)
        left_partition_size = (total_length + 1) // 2
        
        left, right = 0, len(nums1)
        while left <= right:
            mid = (left + right) // 2
            nums1_size = mid
            nums2_size = left_partition_size - mid
            
            # boundary number 4개 구하기
            nums1_left = nums1[nums1_size-1] if nums1_size > 0 else float("-inf")
            nums1_right = nums1[nums1_size] if nums1_size < len(nums1) else float("inf")
            nums2_left = nums2[nums2_size-1] if nums2_size > 0 else float("-inf")
            nums2_right = nums2[nums2_size] if nums2_size < len(nums2) else float("inf")
            
            if nums1_left > nums2_right:
                right = mid - 1
            elif nums2_left > nums1_right:
                left = mid + 1
            else:
                if total_length % 2 == 1:
                    return max(nums1_left, nums2_left)
                else:
                    return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2