class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        operations = []
        target_index = 0
        
        # Stream numbers from 1 to n
        for num in range(1, n + 1):
            # If we already matched all numbers in target, stop immediately
            if target_index == len(target):
                break
                
            # Every number from the stream must be pushed first
            operations.append("Push")
            
            # If the number matches the current target item, keep it
            if num == target[target_index]:
                target_index += 1
            else:
                # If it doesn't match, we must immediately pop it out
                operations.append("Pop")
                
        return operations

        