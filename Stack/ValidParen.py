class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        if len(s) % 2 == 1:
            return False

        stack = []
        brackets = {")" : "(", "}" : "{" , "]" : "["}

        for p in s:
            if p in brackets.values():
                stack.append(p)
            elif len(stack) == 0 or brackets[p] != stack.pop():
                return False
        
        return stack == []

        # for p in s:
        #     if p == "(" or p == "{" or p == "[":
        #         stack.append(p)

        #     elif p == ")" :
        #         if stack == [] or stack[-1] != "(":
        #             return False
        #         else:
        #             stack.pop()

        #     elif p == "}":
        #         if stack == [] or stack[-1] != "{":
        #             return False
        #         else:
        #             stack.pop()
            
        #     elif p == "]":
        #         if stack == [] or stack[-1] != "[":
        #             return False
        #         else:
        #             stack.pop()
            
            
        # return stack == []


            
