class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        # Count how many students prefer type 0 and type 1
        count_0 = students.count(0)
        count_1 = students.count(1)
        
        for sandwich in sandwiches:
            if sandwich == 0:
                if count_0 > 0:
                    count_0 -= 1  # A student takes the circular sandwich
                else:
                    # No student left wants a circular sandwich, gridlock!
                    break
            else: # sandwich == 1
                if count_1 > 0:
                    count_1 -= 1  # A student takes the square sandwich
                else:
                    # No student left wants a square sandwich, gridlock!
                    break
                    
        # The remaining students who could not eat
        return count_0 + count_1

        