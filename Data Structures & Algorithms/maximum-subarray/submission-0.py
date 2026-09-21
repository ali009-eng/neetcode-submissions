class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cursum = 0
        maxsum = nums[0]
        for i, v in enumerate(nums):
            if cursum < 0:
                cursum = 0
            cursum += v
            if cursum > maxsum:
                maxsum = cursum
        return maxsum