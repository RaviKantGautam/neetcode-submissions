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
                print("b", b)
                print("stack=", stack)
                # print("bracker_hash", bracker_hash[b])
                if stack and bracker_hash[b] != stack.pop():
                    return False
        print("stack=", stack)
        return True if len(stack) == 0 else False
        