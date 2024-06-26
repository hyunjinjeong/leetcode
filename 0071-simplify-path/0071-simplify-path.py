class Solution:
    def simplifyPath(self, path: str) -> str:
        # 바로 떠오르는건 stack? 왜냐면 ".."를 만나면 바로 앞의 경로를 빼줘야 함
        # ".."랑 "..." 구분 때문에 "/"로 스플릿하는게 편하긴 한데... 쓰면 안 되겠지?
        # total_path = []
        # current_path = []

        # i = 0
        # while i < len(path):
        #     if path[i] == "/":
        #         if current_path:
        #             total_path.append("".join(current_path))
        #         current_path = []
        #         while i < len(path) and path[i] == "/":
        #             i += 1
        #     elif path[i] == "." and not current_path:
        #         if i == len(path) - 1 or path[i+1] == "/": # "."로 끝난 경우
        #             # 현재 경로니까 아무 것도 안 넣으면 됨. i만 적당히 증가
        #             i += 1
        #         elif path[i+1] == "." and (i + 1 == len(path) - 1 or path[i+2] == "/"): # ".."인 경우
        #             if total_path:
        #                 total_path.pop() # 최근 경로 하나 빼기
        #             i += 2
        #         else:
        #             while i < len(path) and path[i] == ".":
        #                 current_path.append(path[i])
        #                 i += 1
        #     else:
        #         current_path.append(path[i])
        #         i += 1
        
        # if current_path:
        #     total_path.append("".join(current_path))
        
        # return "/" + "/".join(total_path)

        stack = []
        curr = []

        def is_single_dot(st):
            return len(st) == 1 and st[0] == "."

        def is_double_dot(st):
            return len(st) == 2 and st[0] == "." and st[1] == "."

        for c in path + "/":
            if c == "/":
                if is_double_dot(curr):
                    if stack: stack.pop()
                elif curr and not is_single_dot(curr):
                    stack.append("".join(curr))
                curr = []
            else:
                curr.append(c)
        
        return "/" + "/".join(stack)
                    