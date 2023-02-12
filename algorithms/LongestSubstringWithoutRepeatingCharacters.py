class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        substring = ''
        maxLength = 0

        for char in s:

            if char not in substring: 
                substring += char
            else:
                substring = substring[substring.index(char)+1:]
                substring += char
                
            
            if len(substring) > maxLength:
                maxLength = len(substring)

        return maxLength