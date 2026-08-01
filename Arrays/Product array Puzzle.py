from typing import List
class Solution:
    def productExceptSelf(self, arr):
        n=len(arr)
        ans=[1]*n
        leftPro=1
        for i in range(n):
            ans[i]=leftPro
            leftPro*=arr[i]
        rightPro=1
        for i in range(n-1,-1,-1):
            ans[i]*=rightPro
            rightPro*=arr[i]
        return ans
            
        
        
