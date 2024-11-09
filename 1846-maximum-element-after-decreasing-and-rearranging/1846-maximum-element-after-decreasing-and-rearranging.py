class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        # sort -> 첫 번째 값을 1로 두고, 그 다음부터는 prev + 1보다 크면 prev + 1로 만드는 걸 반복하면 될 듯
        # 이걸 O(N)으로 못 하려나?
        arr.sort()
        arr[0] = 1

        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1] + 1:
                arr[i] = arr[i - 1] + 1

        return arr[-1]