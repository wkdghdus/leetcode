class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        #create a dictionary to store the number of times each character appears in s
        sDict = {}
        tDict = {}
        for char in s:
            if char in sDict:
                sDict[char] += 1
            else:
                sDict[char] = 1
        
        #create a dictionary to store the number of times each character appears in t
        for char in t:
            if char in tDict:
                tDict[char] += 1
            else:
                tDict[char] = 1
        
        #check if the dictionaries are the same
        
        if len(sDict) != len(tDict):
            return False
        
        for key in sDict:
            if key not in tDict:
                return False
            elif sDict[key] != tDict[key]:
                return False
        
        return True

        # #check if each unique character in s and t are the same
        # for char in s:
        #     if char not in t:
        #         return False
            
        #     #remove the character from t
        #     t = t.replace(char, "", 1)

        #     print(t)
        
        # return True