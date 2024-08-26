class Solution:
    def minSwaps(self, s: str) -> int:
        # balanced라는게 결국.. 브라켓이 valid하면 되는거 같은데?
        # "", [], [[]], [[][]], [[]]
        # 반대로 브라켓이 유효한데 balanced가 아닌 경우가 있으려나? 없는거 같음.
        # n이 10^5까지 가는걸 보면 backtracking은 아니고..
        # 시간복잡도를 n이나 nlogn 정도에 해결할 수 있어야 할 것 같음. DP?
        # DP로 어떻게 풀지...
        # swap이니까 s[i], s[j]를 바꿔야 되는데
        # 일단 DP라고 확정은 해놓지 말고
        # stack으로 풀 수도 있으려나? 요런 문제는 스택이 자주 쓰이는데
        # 뭔가 그리디하게 못 하나?
        # [의 갯수와 ]의 갯수가 정확히 n // 2개로 같다는 점을 이용할 수 있으려나?
        # ]]][[[ 이면.. 카운트를 세보면 -1 -2 -3 -2 -1 0.
        # 0, 5를 바꿔보면 []][[] -> 1 0 -1 0 1 0
        # 다시 2,3을 바꾸면 [][][] -> 1 0 1 0 1 0.
        # 그럼 세다가 -가 되면 스왑을 해볼까?
        # 스왑을 하면... -1에서 스왑을 하면..? +2니까 1이 됨
        # 오른쪽에선 [를 세고 왼쪽에서 ]를 세볼까?
        # 그럼 ]][[[]라고 할 때
        # 처음에 스왑은 0이랑 4가 되겠지..
        # 그럼 [][[]]
        # 끝이네?

        
        def find_last_opening_bracket_index(curr):
            for i in range(curr - 1, -1, -1):
                if arr[i] == "[":
                    return i
        
        arr = list(s)
        N = len(arr)

        last_opening_bracket_index = find_last_opening_bracket_index(N)
        count = 0
        res = 0

        for i, c in enumerate(arr):
            if c == "[":
                count += 1
            else:
                count -= 1
            
            if count < 0: # ]가 더 많아지면 가장 오른쪽에 있는 [와 스왑
                arr[i], arr[last_opening_bracket_index] = arr[i], arr[last_opening_bracket_index]
                count += 2
                res += 1
                last_opening_bracket_index = find_last_opening_bracket_index(last_opening_bracket_index)

        return res