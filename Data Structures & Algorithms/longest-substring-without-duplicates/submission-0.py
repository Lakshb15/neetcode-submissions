class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = []
        maxlen = 0 

        for i in range(len(s)):
            if s[i] not in substring:
                substring.append(s[i])
                maxlen = max(maxlen, len(substring))
            else:
                index = substring.index(s[i])
                substring = substring[index + 1 :]
                substring.append(s[i])
                maxlen = max(maxlen, len(substring))
        
        return maxlen