class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        nums.sort()
        for i,n in enumerate(nums):
            if i + 1 < len(nums) and n - (nums[i+1] - 1) != 0:
                return n + 1
        
        if nums[-1] != len(nums):
            return len(nums)

        return 0

        
