class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        trag = target
        sol = []
        for i,v in enumerate(nums):
            for k,j in enumerate(nums):
                if i != k and v + j == target:
                    sol = [i, k]
                    sol.sort()
                    return sol