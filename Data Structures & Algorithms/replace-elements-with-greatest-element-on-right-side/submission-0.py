class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)-1):
            maximum = []
            for j in range(i+1, len(arr)):
                maximum.append(arr[j])

            arr[i] = max(maximum)
        arr[-1] = -1

        return arr