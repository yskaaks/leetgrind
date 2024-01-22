class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        for day, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                prev_day = stack.pop()
                answer[prev_day] = day - prev_day
            stack.append(day)
        return answer



        # for day in range(len(temperatures)):
        #     for future in range(day + 1, len(temperatures)):
        #         if temperatures[future] > temperatures[day]:
        #             answer[day] = future - day
        #             break
        # return answer