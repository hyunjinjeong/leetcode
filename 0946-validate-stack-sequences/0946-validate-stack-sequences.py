class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        # 이건 그냥 시뮬레이션을 해보면 되지 않을까?
        N = len(pushed)
        
        stack = []

        pop_index = 0
        for push_index in range(N):
            stack.append(pushed[push_index])
            while stack and stack[-1] == popped[pop_index]:
                stack.pop()
                pop_index += 1
        
        return len(stack) == 0