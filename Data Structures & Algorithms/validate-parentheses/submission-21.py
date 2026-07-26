class Solution:
    def isValid(self, s: str) -> bool:
        bracker_hash = {
            "]": "[",
            "}": "{",
            ")": "("
        }
        stack = []
        for b in s:
            if not stack or b in bracker_hash.values():
                stack.append(b)
            else:
                if stack and bracker_hash[b] != stack.pop():
                    return False
        return True if len(stack) == 0 else False
        