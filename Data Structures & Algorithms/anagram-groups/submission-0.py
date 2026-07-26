class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_hashed = {}
        for i in strs:
            word = "".join(sorted(i))
            if word in grouped_hashed.keys():
                grouped_hashed[word].append(i)
            else:
                grouped_hashed[word] = [i]
        return [i for i in grouped_hashed.values()]
