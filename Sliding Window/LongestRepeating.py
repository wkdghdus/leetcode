class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        #declare a dictionary to save the count of the characters within the window
        count = {}
        
        #left pointer
        l = 0
        #max frequency
        maxf = 0

        #go through the string, r is the right pointer
        for r in range(len(s)):

            #use the letter of the right pointer as the key and increment the value 
            count[s[r]] = 1 + count.get(s[r], 0)
            #change the max frequency accordingly
            maxf = max(maxf, count[s[r]])

            #if the length of the window minus the max frequency = the letters that must be changed
            #if that count is bigger the possible operation that we can perform then reduce the window
            #and reduce the count of the frequency of the left pointer value
            if (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

        return (r - l + 1)