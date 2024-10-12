class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # binary code는 길이가 k인 모든 binary 표현
        # k = 4면 -> 0000 0001 0010 0011 0100 0101 0110 0111 1000 ... 해서 16개
        # 이런 식으로 2**k개가 나온다.
        # 음 근데 k가 정해져 있으니까.. substring 중 길이가 k 미만인 것들은 고려하지 않아도 됨
        # 길이 k의 sliding window로 돌면서, binary code를 하나씩 확인하면 될 것 같은데
        # 돌면서 갯수가 2**k가 되면 True, 아니면 False
        # 근데 갯수는..? 그냥 set을 쓰면 되려나?
        binary_codes = set()
        for i in range(len(s) - k + 1):
            sub_str = s[i:i + k]
            binary_codes.add(sub_str)
            if len(binary_codes) == 2 ** k:
                return True
        return False