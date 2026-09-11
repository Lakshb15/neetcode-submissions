class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        RightMax = -1

        for i in range(len(arr)-1,-1,-1):
            temp = arr[i]
            arr[i] = RightMax
            RightMax = max(RightMax, temp)
        return arr