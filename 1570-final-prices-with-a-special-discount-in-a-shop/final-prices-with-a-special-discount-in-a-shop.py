class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        # Stack to store indices of items waiting for a discount
        stack = []
        
        for i in range(len(prices)):
            # While the stack isn't empty and the current price can act as a discount
            # for the item at the index stored at the top of our stack
            while stack and prices[i] <= prices[stack[-1]]:
                # Pop the index and apply the discount
                prev_index = stack.pop()
                prices[prev_index] -= prices[i]
            
            # Push the current index onto the stack
            stack.append(i)
            
        return prices

        