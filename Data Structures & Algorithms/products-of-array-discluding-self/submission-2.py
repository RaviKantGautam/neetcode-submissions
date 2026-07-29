class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        res = [0]*n

        for i in range(n):
            prd = 1
            for j in range(n):
                if i==j:
                    continue
                prd*=nums[j]
            res[i] = prd
        return res