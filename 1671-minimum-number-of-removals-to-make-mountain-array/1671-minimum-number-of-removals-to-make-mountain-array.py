class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        # 특정 index를 기준으로 해당 index가 max고, 왼쪽은 strictly increasing, 오른쪽은 strictly decreasing 해야 함
        # max를 제거해야 할 경우도 있을까? 1234421 이런 식이면 max를 없애야 함.. 그럼 일단 max가 1개만 존재하도록 나머지는 제거해야 하나?
        # 그렇게 제거하고 나면? 특정 array가 monotonically increasing 이거나 decreasing
        # len(nums) - (len(increasing) + len(decreasing) - 1).
        # 이렇게 보니 LIS 문제임
        N = len(nums)

        def bisect_left(target, arr):
            lo, hi = 0, len(arr)
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if target <= arr[mid]:
                    hi = mid
                else:
                    lo = mid + 1
            return lo

        def get_lis_lengths(target_arr):
            lis = [1] * N
            arr = [target_arr[0]]

            for i in range(1, N):
                index = bisect_left(target_arr[i], arr)
                if index == len(arr):
                    arr.append(target_arr[i])
                else:
                    arr[index] = target_arr[i]
                lis[i] = len(arr)
            
            return lis
        
        lis_lengths = get_lis_lengths(nums)
        lds_lengths = get_lis_lengths(list(reversed(nums)))

        res = N
        for i in range(N):
            lis_length, lds_length = lis_lengths[i], lds_lengths[N - 1 - i]
            if not (lis_length > 1 and lds_length > 1):
                continue
            res = min(res, N - (lis_length + lds_length - 1))
        return res
