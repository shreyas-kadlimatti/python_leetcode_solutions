class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        def my_gcd(x,y):
            while y!=0:
                x=y 
                y=x%y
                return x

        gcd=numsDivide[0]
        for i in range(1,len(numsDivide)):
            gcd=math.gcd(gcd,numsDivide[i])
        nums.sort()
        for i in range(len(nums)):
            if gcd%nums[i]==0:
                return i
            
        return -1

        