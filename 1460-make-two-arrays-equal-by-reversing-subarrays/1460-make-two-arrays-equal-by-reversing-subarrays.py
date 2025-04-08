class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        # 아무 subarray나 reverse할 수 있다는 건 순서를 마음대로 재배치할 수 있다는 뜻 아닌가..
        return sorted(target) == sorted(arr)