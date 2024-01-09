class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        def neighbors(node):
            for i in range(4):
                num = int(node[i])
                next_num = (num + 1) % 10
                yield node[:i] + str(next_num) + node[i+1:]
                next_num = (num - 1 + 10) % 10
                yield node[:i] + str(next_num) + node[i+1:]
        
        dead_ends = set(deadends)
        q = collections.deque([('0000', 0)])
        seen = set(['0000'])

        while q:
            node, depth = q.popleft()
            if node == target:
                return depth
            if node in dead_ends:
                continue
            
            for n in neighbors(node):
                if n not in seen:
                    seen.add(n)
                    q.append((n, depth + 1))
            
        return -1