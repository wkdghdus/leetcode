class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        #second approach, not using built in functionns
        left = 0
        right = len(s)-1

        while left < right:
            while left < right and not self.isAlphaNumeric(s[left]):
                left += 1
            while left < right and not self.isAlphaNumeric(s[right]):
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1

        return True


    def isAlphaNumeric(self, c):
        return (ord('0') <= ord(c) <= ord('9')) or (ord('a') <= ord(c) <= ord('z')) or (ord('A') <= ord(c) <= ord('Z'))


        # #first clean the string to alphanumeric characters only and convert to lower case
        # s = ''.join(e for e in s if e.isalnum()).lower()
       
        # #first two pointers approach. 
        # left = 0
        # right = len(s)-1
        # while left < right:
        #     if s[left] != s[right]:
        #         return False
        #     left += 1
        #     right -= 1
        
        # return True
    
