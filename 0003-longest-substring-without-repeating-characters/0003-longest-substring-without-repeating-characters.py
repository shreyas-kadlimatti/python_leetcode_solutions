class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
       
        # lent=[0]*100
        # for i in range(0,len(s)):
        #      ss=""
        #     for j in range(i,len(s)):
        #         if i not in sss:
        #             ss+=i
        #         else:
        #             break
        #     lent.append(len[ss])
        # return max(a)
        
        maxl=0 
        left=0 
        unqset=set()
        for right in range(len(s)):
            while s[right] in unqset:
                unqset.remove(s[left])
                left+=1 
            unqset.add(s[right])
            maxl=max(maxl,right-left+1)
        return maxl