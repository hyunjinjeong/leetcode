class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        # xor을 prefix sum처럼 보관하면 되겠고
        # k는 XOR을 최대화 한다는건 prefix sum에 저장된 값의 비트를 다 뒤집은 값이면 될 듯?
        # 근데 숫자는 왜 하필 정렬되어 있을까? ㅁㄹ
        # 일단 해보자. 쿼리를 거꾸로 돌리면 prefix sum도 없어도 될 듯
        res = [0] * len(nums)
        max_xor = 2 ** maximumBit - 1
        
        curr_xor = 0
        for i in range(len(nums)):
            curr_xor ^= nums[i]
            res_index = len(nums) - 1 - i

            # 이제 이 curr_xor에 어떤 숫자를 xor해서 최댓값이 나와야 함.
            # XOR 최댓값이 2 ** bit - 1이니까, 이거랑 prefix랑 xor한 값을 쓰면 되는구나
            # 아래처럼 구하지 않아도 됨.
            res[res_index] = max_xor ^ curr_xor
            
            # target_num = 0
            # num = curr_xor
            # bit = 0
            # while bit < maximumBit:
            #     if num & 1 == 0:
            #         target_num |= (1 << bit)
                
            #     res[res_index] = target_num
            #     num >>= 1
            #     bit += 1

        return res
