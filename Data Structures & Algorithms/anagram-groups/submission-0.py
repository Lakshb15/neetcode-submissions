class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for word in strs:
            a = sorted(word)
            key = "".join(a)
            if key not in dic:
        
                dic[key] = []
            dic[key].append(word)
        return list(dic.values())