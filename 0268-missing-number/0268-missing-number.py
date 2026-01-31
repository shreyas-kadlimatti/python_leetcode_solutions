class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s_o_n=(len(nums)*(len(nums)+1))/2
        b=sum(nums)
        return int(s_o_n-b)