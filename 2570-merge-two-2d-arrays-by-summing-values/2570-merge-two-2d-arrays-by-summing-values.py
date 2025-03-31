class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        res = []

        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            index1, num1 = nums1[i]
            index2, num2 = nums2[j]

            if index1 == index2:
                res.append([index1, num1 + num2])
                i += 1
                j += 1
            elif index1 < index2:
                res.append([index1, num1])
                i += 1
            else:
                res.append([index2, num2])
                j += 1
            
        while i < len(nums1):
            res.append(nums1[i])
            i += 1
        while j < len(nums2):
            res.append(nums2[j])
            j += 1

        return res