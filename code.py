class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pointer1,pointer2 = 0,0
        while pointer1<len(s)and pointer2<len(t):
            if s[pointer1]==t[pointer2]:
                pointer1+=1 # Move pointer 1 only if a character match
            pointer2+=1 # Always move pointer 2
        return pointer1==len(s) # True if we matches all of 's'
