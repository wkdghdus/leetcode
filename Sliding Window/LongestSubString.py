class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        subst = []
        longest = 0

        for i in range(len(s)):
            while s[i] in subst:
                subst.pop(0)
            
            subst.append(s[i])

            longest = max(longest, len(subst))

        return longest
            