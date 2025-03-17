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

        # 만개 시작한 꽃 개수
        flower_index = 0
        for time, index in sorted_people:
            while flower_index < len(flowers) and starts[flower_index] <= time:
                flower_index += 1
            res[index] = flower_index
        
        # 종료된 꽃 개수
        flower_index = 0
        for time, index in sorted_people:
            while flower_index < len(flowers) and ends[flower_index] < time:
                flower_index += 1
            res[index] -= flower_index

        return res