class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        # 2, 4, 6 / 2면
        # 2 / 4 / 6 / 2 4 / 2 6 / 4 6 / 2 4 6
        # 이 중에 두 숫자의 차가 k인 경우가 없어야 함
        # 일단 sorting을 해야겠고...
        # 아 바로 전 숫자만 보면 안된다. 4 5 7 같은 경우. 그러면 sorting 필요 없음.
        # 그 다음에는 1. 다 만들고 검증, 2. 만들면서 검증이 있는데
        # 1번은 쉽고... 2번이 더 효율적이겠지?

        # 숫자가 2, 5고 k가 3이면..
        # 

        def backtrack(start, counter):
            res = 1
            
            for i in range(start, len(nums)):
                counter[nums[i]] += 1
                if counter[nums[i] - k] == 0 and counter[nums[i] + k] == 0:
                    res += backtrack(i + 1, counter)
                counter[nums[i]] -= 1
            
            return res
        
        return backtrack(0, collections.Counter()) - 1 # []인 경우 제외