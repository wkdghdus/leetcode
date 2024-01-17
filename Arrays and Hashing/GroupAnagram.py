class Solution(object):

    # def toDict(self, word):
    #     wordDict = [0] * 26

    #     for letter in word:
    #         wordDict[ord(letter) - ord("a")] += 1
            
    #     return wordDict

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        retHash = {}

        for word in strs:
            sortedWord = "".join(sorted(word))

            if sortedWord in retHash:
                retHash[sortedWord].append(word)
            else:
                retHash[sortedWord] = [word]   

        return retHash.values()

    #     anagramHash = {}

    #     for word in strs:
    #         wordDict = self.toDict(word)

    #         if tuple(wordDict) in anagramHash:
    #             anagramHash[tuple(wordDict)].append(word)
    #         else:
    #             anagramHash[tuple(wordDict)] = [word]
            
    #     return anagramHash.values()

    
