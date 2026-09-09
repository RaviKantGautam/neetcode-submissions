class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen, left = 0, 0
        charmap = {}

        for right, char in enumerate(s):
            if char in charmap and charmap[char] >= left:
                left = charmap[char]+1
            charmap[char] = right
            maxlen = max(maxlen, right-left+1)
        return maxlen