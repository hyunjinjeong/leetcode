class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        # 특정 날짜에 몇 개의 꽃이 만개해있는지 알아야 함. 즉 overlapping interval의 수를 구하는 문제
        START, END = 0, 1

        # 만개 시작한 꽃 - 종료된 꽃
        # 각각을 prefix sum 느낌으로 구할 수 있으려나?
        starts = sorted([flowers[i][START] for i in range(len(flowers))])
        ends = sorted([flowers[i][END] for i in range(len(flowers))])
        sorted_people = sorted([(people[i], i) for i in range(len(people))])
        
        res = [0] * len(people)

        start_flower_index = 0
        end_flower_index = 0
        for time, index in sorted_people:
            # 여기를 binary search를 사용할 수 있겠네
            while start_flower_index < len(flowers) and starts[start_flower_index] <= time:
                start_flower_index += 1
            while end_flower_index < len(flowers) and ends[end_flower_index] < time:
                end_flower_index += 1

            res[index] = start_flower_index - end_flower_index

        return res