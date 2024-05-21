class Solution(object):
    
    
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        stack = []
        result = []

        def foo(open, close):
            if open == close == n:
                result.append("".join(stack))
                return

            if open < n:
                stack.append("(")
                foo(open+1, close)
                stack.pop()
                
            if close < open:
                stack.append(")")
                foo(open, close + 1)
                stack.pop()

        foo(0,0)

        return result
