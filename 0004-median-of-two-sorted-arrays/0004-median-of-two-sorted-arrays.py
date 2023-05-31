class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) < len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        
        lo, hi = 0, len(nums2) * 2
        while lo <= hi:
            mid2 = (lo + hi) // 2
            mid1 = len(nums1) + len(nums2) - mid2

            l1 = float("-inf") if mid1 == 0 else nums1[(mid1-1)//2]
            l2 = float("-inf") if mid2 == 0 else nums2[(mid2-1)//2]
            r1 = float("inf") if mid1 == len(nums1) * 2 else nums1[mid1//2]
            r2 = float("inf") if mid2 == len(nums2) * 2 else nums2[mid2//2]

            if l1 > r2:
                lo = mid2 + 1
            elif l2 > r1:
                hi = mid2 - 1
            else:
                return (max(l1, l2) + min(r1, r2)) / 2