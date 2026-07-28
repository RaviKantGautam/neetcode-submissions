class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        for i in range(len(nums)):
            res.append(nums[:i]+nums[i+1:])
        for j in range(n):
            prd = 1
            for k in res[j]:
                prd*=k
            res[j] = prd
        return res