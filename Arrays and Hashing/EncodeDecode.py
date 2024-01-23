class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = ""
        for word in strs:
            encode += str(len(word)) + "#" + word
        return encode

    def decode(self, s: str) -> List[str]:
        decode = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
        
            decode.append(s[j+1:j+length+1])
            i = j + length + 1
        
        return decode