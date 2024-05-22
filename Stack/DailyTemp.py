class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        
        res = [0] * len(temperatures)
        stack = []  #temp, ind

        #enumerate through temp since we need the index and the value information. this can be replaced using traditional for loop and using index.
        for ind, temp in enumerate(temperatures):
            
            #while the stack is not empty and current temperature is greater than the previous one, keep popping and update the result.
            while stack and temp > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = ind - stackInd
            stack.append((temp, ind))
        
        return res
