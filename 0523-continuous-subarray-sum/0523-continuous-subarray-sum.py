class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # 뭔가 prefix sum을 쓰는 것 같은데
        # ..? % k 연산한 값을 넣으면 되는구나
        prefix_mod_map = {0: -1}
        
        mod = 0
        for i, num in enumerate(nums):
            mod = (mod + num) % k
            if mod in prefix_mod_map:
                if i - prefix_mod_map[mod] >= 2:
                    return True
            else:
                prefix_mod_map[mod] = i
        
        return False