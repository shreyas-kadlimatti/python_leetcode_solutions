class Solution:
#using Eratosthenes. Time-complexity-(n(log(logn))) and 
# mertens second therome-partial sum of prime num till n is (log(logn))
    def findPrimePairs(self, n: int) -> List[List[int]]:
        
        prime=[True]*(n+1)
        for i in range(2,int(n**0.5)+1):
            if prime[i]==True:
                for j in range(i*i,n+1,i):
                    prime[j]=False 
        l=[]
        for i in range(2,(n//2+1)):
                if prime[i] and prime[n-i]:
                    l.append([i,n-i])
        return (l)         

#other approach 
        
    # prime=[True]*(n+1)
    # for i in range(2,int(n**0.5)+1):
    #     if prime[i]==True:
    #         for j in range(i*i,n+1,i):
    #             prime[j]=False 
    # l=[]
    # for i in range(2,(n//2+1)):
    #         if prime[i] and prime[n-i]:
    #             l.append([i,n-i])
    # return (l)  
