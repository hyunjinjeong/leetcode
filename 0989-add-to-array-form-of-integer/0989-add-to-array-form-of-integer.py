class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        # num이 k보다 크면 문제가 없지만.. 작으면 문제가 된다
        # linked list로 바꾸고 계산하는 방법도 있고
        # 숫자로 바꾸고 다시 list로 바꾸는 방법도 있을 듯
        num_int = 0
        for n in num:
            num_int = num_int * 10 + n

        added_num = num_int + k
        res = []
        while added_num:
            res.append(added_num % 10)
            added_num //= 10
        
        return res[::-1]