class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if len(s) % 2 != 0: return False


        stack = []

        brackets = {')':'(', '}': '{', ']': '['}

        for bracket in s:
            if bracket == '(' or bracket == '{' or bracket == '[':
                stack.append(bracket)
            else:
                if len(stack) == 0 or stack.pop() != brackets[bracket]:
                    return False
            
        return len(stack) == 0
