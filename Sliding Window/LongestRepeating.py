class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        #dictionary for the frequency
        freq = {}
        l = 0
        r = 1
        res = 0
        maxFreq = 0

        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r], 0)
            maxFreq = max(maxFreq, freq[s[r]])

            if (r-l+1) - maxFreq > k: 
                freq[s[l]] -= 1
                l += 1
            
            res = max(res, r-l+1)

        return res
            
        