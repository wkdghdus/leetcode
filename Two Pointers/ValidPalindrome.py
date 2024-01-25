class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        s = s.lower()
        for letter in s:
            if not letter.isalnum():
                s = s.replace(letter, '')
        
        for i in range(len(s)/2):
            if s[i] != s[len(s)-i-1]:
                return False
        
        return True