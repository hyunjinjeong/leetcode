class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # count 세서 하나씩 하면 되는거 아닌가
        # 2 -> 4, 3 -> 3, 4 -> 2
        
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        res = 0
        for num in count:
            num_count = count[num]
            if num_count == 1:
                return -1
            
            curr = 0
            while num_count > 4:
                num_count -= 3
                curr += 1
            
            if num_count == 4:
                curr += 2
            else:
                curr += 1
            
            res += curr

            # 근데 여기서 2개짜리를 쓸지 4개짜리를 쓸지는 어떻게 정하지
            # 4는 2 2고 5는 2 3, 6은 3 3, 7은 3 2 2, 8은 3 3 2, 9는 3 3 3, 10은 3 3 2 2
            # 11은 3 3 3 2, 12는 3333, 13은 33322
            # 4 이상까지는 3으로 빼고 그 다음엔 2랑 3 중에 하나 정하면 될 듯?
        
        return res