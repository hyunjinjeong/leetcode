class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        # 새로 들어온 book이 현재 shelf의 높이를 증가시키면 새로운 shelf로 넣는게 낫나?
        # 흠.. 그건 아닌듯하고
        # DP..? 한 줄에 들어갈 수 있는 책의 수는 정해져 있다.
        # DP는 어떻게 정할까
        # i번째 book이 있을 때.. 그 book을 현재 shelf에 넣을 수도 있고 다음 shelf에 넣을 수도 있음.
        # 근데 현재 shelf에 아무 책도 없을 때는 무조건 현재 shelf에 넣어야 함.
        # 혹은 현재 shelf의 길이를 더하면 shelfWidth보다 커지면 무조건 다음 shelf에 넣어야 함.
        memo = {}

        @cache
        def dfs(i, curr_width, curr_height):
            if i == len(books):
                return curr_height
            if (i, curr_width) in memo:
                return memo[(i, curr_width)]
        
            width, height = books[i]
            
            use_next_shelf = curr_height + dfs(i + 1, width, height)
            if curr_width + width > shelfWidth: # 못 넣으면
                return use_next_shelf

            use_curr_shelf = dfs(i + 1, curr_width + width, max(height, curr_height))
            memo[(i, curr_width)] = min(use_curr_shelf, use_next_shelf)
            return memo[(i, curr_width)]
        
        return dfs(0, 0, 0)
