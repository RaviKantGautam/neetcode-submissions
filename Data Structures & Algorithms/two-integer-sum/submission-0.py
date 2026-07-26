class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices_hash = {}
        for idx, i in enumerate(nums):
            j = target-i
            if j in indices_hash.keys():
                return [indices_hash[j], idx]
            indices_hash[i] = idx
        return []