class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # set으로 만들면 되는데.. 이게 맞나?
        # 정렬 후 투포인터를 쓸 수도 있을 듯?
        return set(nums1) & set(nums2)