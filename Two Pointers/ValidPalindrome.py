class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        clean = "".join(char for char in s if char.isalnum()).lower()

        return clean == clean[::-1]

        # top, bot = len(clean)-1, 0

        # while top >= bot:
        #     if clean[top] != clean[bot]: 
        #         return False

        #     top -= 1
        #     bot += 1
            
        
        # return True