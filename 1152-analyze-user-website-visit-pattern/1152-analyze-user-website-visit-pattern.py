class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        # 유저별로 방문한 웹사이트 순서를 구할 수 있음..
        # joe: home -> about -> career
        # james: home -> cart -> maps
        # mary: home -> about -> career
        # 그래프 문제인가..? 근데 연속해서 방문할 필요가 없어서 어떻게 할지 모르겠음
        # 최대 50개니까 전체 경우의 수가 50 * 49 * 48. 할만한데 전체를 대상으로 그냥 다 돌려봐야 하나?
        # def get_pattern_score(pattern):
        #     count = 0
        #     for user in user_visits:
        #         if is_valid_pattern(user, pattern):
        #             count += 1
        #     return count

        # def is_valid_pattern(user, pattern):
        #     visited_count = 0
        #     i, j = 0, 0

        #     user_visit = user_visits[user]
        #     if len(user_visit) < 3:
        #         return False

        #     while i < len(user_visit) and j < len(pattern):
        #         if user_visit[i] == pattern[j]:
        #             visited_count += 1
        #             i += 1
        #             j += 1
        #         else:
        #             i += 1
                
        #         if visited_count == 3:
        #             return True
            
        #     return False

        # # 유저별 방문 순서 계산
        # user_visits = collections.defaultdict(list)
        # sorted_list = sorted(zip(username, timestamp, website), key=lambda tup: tup[1])
        # for i in range(len(username)):
        #     user, time, site = sorted_list[i]
        #     user_visits[user].append(site)
                
        # # 모든 경우의 수 계산
        # distinct_websites = list(sorted(set(website)))
        # N = len(distinct_websites)
        
        # curr_score, curr_pattern = 0, []
        # for i in range(N):
        #     for j in range(N):
        #         for k in range(N):
        #             pattern = [distinct_websites[i], distinct_websites[j], distinct_websites[k]]
        #             pattern_score = get_pattern_score(pattern)
        #             if pattern_score > curr_score:
        #                 curr_score = pattern_score
        #                 curr_pattern = pattern

        # return curr_pattern

        # 이게 전체 경우의 수를 구할 필요가 없이, 유저 방문 패턴의 수만 세면 되는구나
        user_visits = collections.defaultdict(list)
        sorted_list = sorted(zip(username, timestamp, website), key=lambda tup: tup[1])
        for i in range(len(username)):
            user, time, site = sorted_list[i]
            user_visits[user].append(site)
        
        pattern_count = collections.defaultdict(int)
        for user in user_visits:
            patterns = set()

            path = user_visits[user]
            for i in range(len(path)):
                for j in range(i + 1, len(path)):
                    for k in range(j + 1, len(path)):
                        patterns.add((path[i], path[j], path[k]))
            
            for pattern in patterns:
                pattern_count[pattern] += 1
        
        max_count, res = 0, []
        for pattern in sorted(pattern_count):
            if pattern_count[pattern] > max_count:
                max_count = pattern_count[pattern]
                res = [pattern[0], pattern[1], pattern[2]]
        
        return res
