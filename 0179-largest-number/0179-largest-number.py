class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # sorting & greedy라..?
        # 그럼 무슨 방법을 정해서 그 순서대로 쭉 하면 된다는 것.
        # string으로 변환 후 비교까진 맞았는데... 단순히 두개 비교하면 됐었음.
        for i in range(len(nums)):
            nums[i] = str(nums[i])
        
        def compare(a, b):
            if a + b < b + a:
                return 1 # 1이면 sorting 후 후순위. 즉 뒤로 온다는 뜻
            else:
                return -1
        
        sorted_nums = sorted(nums, key=functools.cmp_to_key(compare))
        # int로 한번 더 묶는 건 엣지 케이스 [0, 0] 같은 경우 처리.
        return str(int("".join(sorted_nums)))