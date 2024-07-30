class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26

        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord("a")] += 1
            s2Count[ord(s2[i]) - ord("a")] += 1

        matches = 0

        for i in range(26):
            matches += 1 if s1Count[i] == s2Count[i] else 0

        l = 0

        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord("a")

            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord("a")
            
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            
            l += 1

        return matches == 26




        # r = len(s1)
        # freqHash = {}
        # res = False

        # for c in s1:
        #     freqHash[c] = 1 + freqHash.get(c,0)

        # for l in range(len(s2)-len(s1)+1):

        #     subWindow = s2[l:r]
            
        #     for key in freqHash:

        #         if key in subWindow:
        #             res = True
        #             subWindow = subWindow.replace(key, '', freqHash[key])
        #         else:
        #             res = False
        #             break

        #     if not subWindow == "":
        #         res = False
                        
        #     if res:
        #         break

        #     r += 1
        
        # return res
    
