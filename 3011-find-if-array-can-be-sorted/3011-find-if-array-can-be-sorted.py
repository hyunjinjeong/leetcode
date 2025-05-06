class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        # set bit 개수에 따라서 그룹화를 한 다음
        # 정렬을 한 다음에 정렬 이후의 숫자와 기존 숫자가 같은 그룹에 있는지 확인하기?
        # 아 adjacent 끼리만 swap할 수 있구나
        # 그럼 group들을 나눠서 각 group 별로 정렬한 결과가 전체 정렬인지 보면 될 듯? 아니면 groups[i - 1]의 max가 groups[i]의 min보다 작은지 확인.
        @cache
        def set_bits(n):
            count = 0
            while n:
                count += n & 1
                n >>= 1
            return count
        
        # groups = []
        # index = -1
        # for num in nums:
        #     if index == -1 or set_bits(num) != set_bits(groups[index][0]):
        #         groups.append([])
        #         index += 1
        #     groups[index].append(num)
        
        # for i in range(1, len(groups)):
        #     if max(groups[i - 1]) > min(groups[i]):
        #         return False

        # return True

        # group을 안 만들어도 되는구나
        prev_max = float("-inf")
        curr_min, curr_max = nums[0], nums[0]
        for num in nums:
            if set_bits(num) == set_bits(curr_min):
                curr_min = min(num, curr_min)
                curr_max = max(num, curr_max)
            else:
                if prev_max > curr_min:
                    return False
                prev_max = curr_max
                curr_min, curr_max = num, num
        
        if prev_max > curr_min:
            return False
        
        return True
