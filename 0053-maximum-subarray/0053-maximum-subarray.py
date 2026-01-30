class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum=float("-inf")
        csum=0 
        for i in nums:
            csum+=i 
            max_sum=max(max_sum,csum)
            if csum<0:
                csum=0 
        return max_sum