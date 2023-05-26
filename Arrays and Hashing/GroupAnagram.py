class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        ttlList = []
        freqDict = {}
        freqDict2 = {}
        anaList = []

        #iterate through words in strs
        for word in strs:
            anaList = [word]
            for char in word:
                    if char in freqDict:
                        freqDict[char] += 1
                    else:
                        freqDict[char] = 1

            for word2 in strs:
            #create a frequency table for each characters in the word
                
                for char in word2:
                    if char in freqDict2:
                        freqDict2[char] += 1
                    else:
                        freqDict2[char] = 1

                for key in freqDict:
                    if key not in freqDict2:
                        break
                    elif freqDict[key] != freqDict2[key]:
                        break
                    elif word2 == word:
                        break
                    else:
                        anaList.append(word2)
                        strs.remove(word2)

                freqDict2 = {}
                    
            ttlList.append(anaList)
            freqDict = {}


        
        return anaList
