from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        final = []
        opt = Counter(nums).most_common(k)
        for pair in opt:
            element = pair[0]
            final.append(element) 
        return final
        