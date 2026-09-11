class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_strs = ""
        for string in strs:
            encoded_strs += str(len(string))
            encoded_strs += "#"
            encoded_strs += string
        return encoded_strs
    
    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0
        while i < len(s):
            length = ""
            while s[i] != "#":
                length += s[i]
                i += 1
            i += 1
            word = ""
            for _ in range(int(length)):
                word += s[i]
                i += 1

            decoded_strs.append(word)
        return decoded_strs
