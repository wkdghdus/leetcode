class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        
        res = [0] * len(temperatures)
        stack = []  #temp, ind

        for ind, temp in enumerate(temperatures):

            while (stack and temp > stack[-1][0]):
                
                stack_temp, stack_ind = stack.pop()
                res[stack_ind] = ind - stack_ind 


            stack.append((temp, ind))
        
        return res
