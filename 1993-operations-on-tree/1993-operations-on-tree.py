class LockingTree:

    def __init__(self, parent: List[int]):
        # parent는 있는데.. upgrade는 자식을 모두 찾아 내려가야 하니까 자식을 관리하고 있어야겠다.
        # 그리고 잠겼는지 여부를 저장하는 배열도 하나 있으면 좋을 것 같고.
        self.parents = parent
        self.locked = [-1] * len(parent)
        self.children = collections.defaultdict(list)
        for i in range(len(parent)):
            if parent[i] == -1: # root
                continue
            # i번째 노드의 부모가 parent[i]면.. parent[i]의 자식이 i라는 뜻
            self.children[parent[i]].append(i)

    def lock(self, num: int, user: int) -> bool:
        if self.locked[num] != -1:
            return False
        self.locked[num] = user
        return True

    def unlock(self, num: int, user: int) -> bool:
        if self.locked[num] != user:
            return False
        self.locked[num] = -1
        return True

    def upgrade(self, num: int, user: int) -> bool:
        if self.locked[num] != -1:
            return False
        # 이 연산들을 매번 수행하는게 맞는가..
        # 노드 갯수도 연산 갯수도 최대 2000개니까 가능할 듯.
        if not self.has_locked_child(num, user):
            return False
        if self.has_locked_parent(num, user):
            return False

        self.locked[num] = user
        self.unlock_all_children(num, user)
        return True
    
    def has_locked_child(self, num, user):
        # 헉 여기서 기존 데이터를 변경하고 있었음;
        stack = []
        for child in self.children[num]:
            stack.append(child)

        while stack:
            child = stack.pop()
            if self.locked[child] != -1:
                return True
            for more_child in self.children[child]:
                stack.append(more_child)
        return False
    
    def has_locked_parent(self, num, user):
        parent = self.parents[num]
        while parent != -1:
            if self.locked[parent] != -1:
                return True
            parent = self.parents[parent]
        return False
    
    def unlock_all_children(self, num, user):
        stack = []
        for child in self.children[num]:
            stack.append(child)

        while stack:
            child = stack.pop()
            self.locked[child] = -1
            for more_child in self.children[child]:
                stack.append(more_child)


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)