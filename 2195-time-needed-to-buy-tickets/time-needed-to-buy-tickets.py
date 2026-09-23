class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        time = 0
        
        for i in range(len(tickets)):
            # If the person is standing before or is person k
            if i <= k:
                time += min(tickets[i], tickets[k])
            # If the person is standing after person k
            else:
                time += min(tickets[i], tickets[k] - 1)
                
        return time

        