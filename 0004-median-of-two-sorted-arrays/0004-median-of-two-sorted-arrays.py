class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 작은 list를 기준으로 mid를 정하고 왼쪽이 left partition이 됨, 큰 list는 half - mid가 왼쪽 partition이 됨.
        # 두 array를 합한 left partition이 전체 조건(left <= right)를 만족할 때까지 binary search...
        # 이 때 조건은 l1 <= r2, l2 <= r1여야 함. 반대면 partition이 잘못된 것
        if len(nums1) > len(nums2):
            # 항상 num1이 더 짧도록.
            return self.findMedianSortedArrays(nums2, nums1)
        
        total_length = len(nums1) + len(nums2)
        left_partition_size = total_length // 2
        
        left, right = 0, len(nums1)
        while left <= right:
            mid = (left + right) // 2
            nums1_size = mid
            nums2_size = left_partition_size - mid
            
            nums1_index, nums2_index = nums1_size - 1, nums2_size - 1
            
            # boundary number 4개 구하기. out of bound 에러 방지 용으로 if문.
            nums1_left = nums1[nums1_index] if nums1_index >= 0 else float("-inf")
            nums1_right = nums1[nums1_index + 1] if nums1_index + 1 < len(nums1) else float("inf")
            nums2_left = nums2[nums2_index] if nums2_index >= 0 else float("-inf")
            nums2_right = nums2[nums2_index + 1] if nums2_index + 1 < len(nums2) else float("inf")
            
            if nums1_left > nums2_right: # partition을 맞추기 위해 small의 size를 줄여야 함.
                right = mid - 1
            elif nums2_left > nums1_right: # 반대로 small의 size를 늘려야 함.
                left = mid + 1
            else:
                if total_length % 2 == 1: # (total + 1) // 2 로 나눴으니 왼쪽 partition의 오른쪽 끝에 mid가 있음
                    return min(nums1_right, nums2_right)
                    # return max(nums1_left, nums2_left)
                else:
                    return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2