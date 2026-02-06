class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        def p():
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
        prime=[True]*(n+1)
        for i in range(2,int(n**0.5)+1):
            if prime[i]==True:
                for j in range(i*i,n+1,i):
                    prime[j]=False 
        pnums=[]
        for i in range(2,len(prime)) :
            if prime[i]==True:
                pnums.append(i)
        res=[]     
        l=0 
        r=len(pnums)-1

        while l<=r:
            if pnums[l]+pnums[r]==n:
                res.append([pnums[l],pnums[r]])
                l=l+1 
                r+1
            elif pnums[l]+pnums[r]>n:
                r=r-1
            else:
                l+=1
                
        return res
