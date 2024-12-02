# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        # self.stack = [(nestedList, 0)]
        self.q = collections.deque(nestedList)
    
    def flatten(self):
        # while self.stack:
        #     curr_list, curr_index = self.stack[-1]
        #     if curr_index == len(curr_list):
        #         self.stack.pop()
        #         continue
            
        #     element = curr_list[curr_index]
        #     if element.isInteger():
        #         break
            
        #     new_list = element.getList()
        #     self.stack[-1] = (curr_list, curr_index + 1)
        #     self.stack.append((new_list, 0))
        while self.q and not self.q[0].isInteger():
            element = self.q.popleft()
            self.q.extendleft(reversed(element.getList()))

    def next(self) -> int:
        # curr_list, curr_index = self.stack[-1]
        # self.stack[-1] = (curr_list, curr_index + 1)
        # return curr_list[curr_index].getInteger()
        return self.q.popleft().getInteger()
    
    def hasNext(self) -> bool:
        # self.flatten()
        # return len(self.stack) > 0
        self.flatten()
        return len(self.q) > 0

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())