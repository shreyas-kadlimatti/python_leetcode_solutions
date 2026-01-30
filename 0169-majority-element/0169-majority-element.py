class Solution:
    def majorityElement(self, nums: List[int]) -> int: 
        m=nums[0]
        c=1
        for i in range(1,len(nums)):
            if m==nums[i]:
                c=c+1 
            else:
                c=c-1 
                if c==0:
                    m=nums[i]
                    c=1 
        return m

     