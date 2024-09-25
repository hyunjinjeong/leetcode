class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        # num이 k보다 크면 문제가 없지만.. 작으면 문제가 된다
        # linked list로 바꾸고 계산하는 방법도 있고
        # 숫자로 바꾸고 다시 list로 바꾸는 방법도 있을 듯
        # reverse 해서 계산하는 방법도 있구나

        num.reverse()
        i = 0

        while k:
            digit = k % 10
            if i < len(num):
                num[i] += digit
            else:
                num.append(digit)
            
            carry = num[i] // 10
            num[i] = num[i] % 10

            k //= 10
            k += carry
            i += 1
        
        num.reverse()
        return num