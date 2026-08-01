class Solution:
    def romanToInt(self, s: str) -> int:
        arr={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        tot=0
        for i in range(0,len(s)):
            if i<len(s)-1 and arr[s[i]]<arr[s[i+1]]:
                tot-=arr[s[i]]
            else:
                tot+=arr[s[i]]
        return tot
        
