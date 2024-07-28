class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # 그냥 시뮬레이션?
        # 먹을 사람을 계산해보면...
        # sandwiches에서 students를 쏙쏙 빼는데
        # 초과된 student는 못 먹는 거니까
        # 걍 갯수만 세서 빼다가 sandwiches에서 하나가 0이 되면 다른쪽은 그때 남은 students 리턴하면 될 듯

        zero_count, one_count = 0, 0
        for student in students:
            if student == 0:
                zero_count += 1
            elif student == 1:
                one_count += 1

        for sandwich in sandwiches:
            if sandwich == 0:
                if zero_count > 0:
                    zero_count -= 1
                else:
                    return one_count
            else:
                if one_count > 0:
                    one_count -= 1
                else:
                    return zero_count
        
        return 0