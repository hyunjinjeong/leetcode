class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 오.. 오른쪽에서부터 돌면 된다
        # 1 3 5 0 0 6 // 2 4
        # 1 3 X 0 5 6 // 2 4
        # 1 3 X 4 5 6 // 2
        # 1 X 3 4 5 6 // 2
        # 1 2 3 4 5 6
        p = m + n - 1
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[p] = nums1[m - 1]
                m -= 1
            else:
                nums1[p] = nums2[n - 1]
                n -= 1
            p -= 1
        
        while n > 0:
            nums1[p] = nums2[n - 1]
            n -= 1
            p -= 1