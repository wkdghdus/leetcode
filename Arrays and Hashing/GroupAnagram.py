class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        ttlDict = {}
        freqDict = {}

        #iterate through words in strs
        for word in strs:
            #create a frequency table for each characters in the word
            for char in word:
                if char in freqDict:
                    freqDict[char] += 1
                else:
                    freqDict[char] = 1

            #append to dictionary
            ttlDict[word] = freqDict
            freqDict = {}

        ttlList = []
        anaList = []
        for word in ttlDict:
            for word2 in ttlDict:
                if len(ttlDict[word]) == len(ttlDict[word2]):
                    for key in ttlDict[word]:
                        if key not in ttlDict[word2]:
                            break
                        elif ttlDict[word][key] != ttlDict[word][key]:
                            break

                        anaList.append(word)

                    ttlList.append(anaList)
        
        return ttlList

