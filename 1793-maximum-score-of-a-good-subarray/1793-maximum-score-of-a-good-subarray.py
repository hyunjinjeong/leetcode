class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        # score는 subarray의 min에 길이를 곱한 값
        # good subarray는 k를 포함하는 범위. inclusive
        # 흠....
        # 일단 good subarray를 구하는 건?
        # k번째 index부터 좌우로 슉슉 늘리면 됨. decision tree처럼..
        # k가 1이면 1, 1 -> 0, 1 / 1 -> 2 -> ... 이런 식으로
        # score를 구하는 건? 길이는 O(1)이고 min은 O(N)인데
        # min을 더 쉽게 구하는 방법이 있나? 
        # k부터 시작해서.. 추가하는 숫자가 더 작으면 min을 업데이트하면서 구하면 O(1)이 될 듯
        # 그러면 score는 O(1)에 가능하고.. max도 구할 수 있고
        # 그냥 DFS로 돌리면 이게.. left, right, min 까지 있어서 시간 복잡도가 너무 큰데
        # 일단 해보자
        # 이거를 어떻게 최적화하지?

        # two pointer를 쓸 수 있으려나
        res = nums[k]

        curr_min = nums[k]
        left, right = k, k 
        while left > 0 and right + 1 < len(nums):
            if nums[left - 1] > nums[right + 1]:
                left -= 1
                curr_min = min(curr_min, nums[left])
                res = max(res, curr_min * (right - left + 1))
            else:
                right += 1
                curr_min = min(curr_min, nums[right])
                res = max(res, curr_min * (right - left + 1))
        
        while left > 0:
            left -= 1
            curr_min = min(curr_min, nums[left])
            res = max(res, curr_min * (right - left + 1))
        
        while right + 1 < len(nums):
            right += 1
            curr_min = min(curr_min, nums[right])
            res = max(res, curr_min * (right - left + 1))
        
        return res