class Solution:
    def majorityElement(self, nums: List[int]) -> int: 
        m=nums[0]
        count=1
        for i in range(1,len(nums)):
            if m==nums[i]:
                count=count+1
            else:
                count=count-1
                if count==0:
                    m=nums[i]
        return m
