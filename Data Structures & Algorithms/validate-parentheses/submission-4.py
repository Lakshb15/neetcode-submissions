class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        pair = {")" : "(", "]": "[", "}": "{"}

        if (len(s)%2) != 0:
            return False

        for char in s:
            if char not in pair:
                stack.append(char)
            else:
                if not stack:
                    return False
                else:
                    if stack[-1] == pair[char]:
                        stack.pop()
                    else:
                        return False
        if stack == []:
            return True
        else:
            return False