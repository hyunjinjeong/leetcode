class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # index를 넣으니까 중복이 생기는구나..
        # 그러면 count를 이용하는 건 어떨까?
        ans = []
        total_count = collections.Counter(nums)

        def backtrack(curr, curr_count):
            if len(curr) == len(nums):
                ans.append(curr[:])
                return
            
            for num in total_count: # unique number만 돌기
                if curr_count[num] == total_count[num]:
                    continue

                curr_count[num] += 1
                curr.append(num)
                backtrack(curr, curr_count)
                curr_count[num] -= 1
                curr.pop()
        
        backtrack([], collections.defaultdict(int))

        return ans