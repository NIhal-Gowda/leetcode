class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        result=[0]*n
        stack=[]
        prev_time=0
        for log in logs:
             fn_id, status, timestamp = log.split(":")
             fn_id = int(fn_id)
             timestamp = int(timestamp)
             if status == "start":
                if stack:
                    result[stack[-1]] += timestamp - prev_time
                stack.append(fn_id)
                prev_time = timestamp
             else:
                result[stack.pop()] += timestamp - prev_time + 1
                prev_time=timestamp+1

        return result
        