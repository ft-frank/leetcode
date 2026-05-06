class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        current_hour = int(current[0:2])
        correct_hour = int(correct[0:2])
        current_min = int(current[3:5])
        correct_min = int(correct[3:5])

        diff_min = correct_min - current_min
        diff_hour = correct_hour - current_hour
        
        diff_time = (diff_hour * 60) + diff_min

        res = 0

        while diff_time > 0:
            if diff_time - 60 >= 0:
                diff_time -= 60
            elif diff_time - 15 >= 0:
                diff_time -= 15
            elif diff_time -5 >= 0:
                diff_time -= 5
            else:
                diff_time -= 1
            res += 1


        return res

