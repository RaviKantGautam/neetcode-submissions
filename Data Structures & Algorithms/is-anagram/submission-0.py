class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq_s = {}
        freq_t = {}
        for i in s:
            freq_s[i] = 1+freq_s.get(i, 0)
        for j in t:
            freq_t[j] = 1+freq_t.get(j, 0)
        
        for key, value in freq_s.items():
            if value != freq_t.get(key, 0):
                return False
        return True
        