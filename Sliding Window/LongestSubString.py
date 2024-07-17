class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        #declare set to save the non duplicating characters (can be any array like data structure)
        charSet = set()
        l = 0   #left pointer
        res = 0 #result

        #iterate through the string, r is the right pointer
        for r in range(len(s)):
            #while the r is in the set, reduce the window by removing the left most character 
            while s[r] in charSet:
                charSet.remove(s[l]) #remove the left most character
                l += 1  #move the left pointer to the right
            #add the character to the set
            charSet.add(s[r])
            #get the max length of the window
            res = max(res, r - l + 1)

        
        return res