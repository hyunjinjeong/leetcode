class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        # sort -> 첫 번째 값을 1로 두고, 그 다음부터는 prev + 1보다 크면 prev + 1로 만드는 걸 반복하면 될 듯
        # # 이걸 O(N)으로 못 하려나?
        # arr.sort()
        # arr[0] = 1

        # for i in range(1, len(arr)):
        #     if arr[i] > arr[i - 1] + 1:
        #         arr[i] = arr[i - 1] + 1

        # return arr[-1]

        N = len(arr)
        counts = [0] * (N + 1)

        for num in arr:
            if num <= N:
                counts[num] += 1
            else:
                counts[N] += 1
        
        res = 1
        for num in range(2, N + 1):
            res = min(res + counts[num], num)
        
        return res
