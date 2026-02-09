class Solution:
    def reverseWords(self, s: str) -> str:
        list=[]
        l=s.split()
        l=l[::-1]
        l=" ".join(l)
        return (l)
        