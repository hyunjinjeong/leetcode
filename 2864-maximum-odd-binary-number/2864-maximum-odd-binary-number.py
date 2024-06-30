class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        # maximum odd binary면 맨 오른쪽에 1이 있어야 함
        # 그럼 1 하나는 맨 오른쪽, 나머지 1들은 맨 왼쪽에 있는 형태면 된다.
        # 1의 갯수 세면 되지 않을까?

        one_count = 0
        for c in s:
            if c == "1":
                one_count += 1
        
        ans = []
        for _ in range(one_count - 1):
            ans.append("1")
        for _ in range(len(s) - one_count):
            ans.append("0")
        
        ans.append("1")

        return "".join(ans)