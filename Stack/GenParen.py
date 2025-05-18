class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        temp_stack = []
        ret = []
        
        def build_paren(open, close):

            if open == close == n:

                ret_str = "".join(temp_stack)
                return ret.append(ret_str)
            
            if open < n:
                temp_stack.append("(")
                build_paren(open+1, close)
                temp_stack.pop()
            
            if close < open:
                temp_stack.append(")")
                build_paren(open, close+1)
                temp_stack.pop()
            
        build_paren(0,0)

        return ret