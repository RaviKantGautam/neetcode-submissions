class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 1, len(numbers)

        while l < r:
            total = numbers[l-1] + numbers[r-1]
            if total == target:
                return [l, r]
            elif total < target:
                l+=1
            else:
                r-=1
        return []
