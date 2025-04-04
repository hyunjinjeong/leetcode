class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        pos = {}
        for i, num in enumerate(arr2):
            pos[num] = i

        return sorted(arr1, key=lambda num: (pos.get(num, len(arr1)), num))