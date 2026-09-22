class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        answer = [0] * n
        stack = []  # Stores indices of days
        
        for i in range(n):
            # While the stack has days and the current temperature is warmer 
            # than the day at the top of the stack
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                # The waiting time is the difference between the indices
                answer[prev_index] = i - prev_index
            
            # Push the current day's index onto the stack
            stack.append(i)
            
        return answer

        