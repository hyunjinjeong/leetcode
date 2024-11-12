class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # 갯수를 세면서.. -가 되면 )를 없애야 함. 없애고 다시 0으로 돌려주고
        # 그러면 +로 마무리되면? 그 남은 만큼 없애면 되지 않을까
        # greedy
        # 아.. 숫자가 아니고 string을 리턴하는구나 ㅋㅋㅋ
        # 그러면 )는 아까처럼 그때그때 없애면 되고
        # (는.. 한번 돌고 숫자를 세서 반대로 돌면서 없애면 될 듯?

        tmp = []

        extra_left_parenthesis_count = 0
        for c in s:
            if c == "(":
                extra_left_parenthesis_count += 1
                tmp.append(c)
            elif c == ")":
                extra_left_parenthesis_count -= 1
                if extra_left_parenthesis_count < 0:
                    extra_left_parenthesis_count = 0
                else:
                    tmp.append(c)
            else:
                tmp.append(c)

        res = collections.deque()
        for i in range(len(tmp) - 1, -1, -1):
            if extra_left_parenthesis_count > 0 and tmp[i] == "(":
                extra_left_parenthesis_count -= 1
            else:
                res.appendleft(tmp[i])
        
        return "".join(res)
