class Solution:
    def missingNumber(self,arr):
        i=0
        while i<len(arr):
            correct=arr[i]-1
            if 1<=arr[i]<=len(arr) and arr[i]!=arr[correct]:
                arr[i],arr[correct]=arr[correct],arr[i]
            else:
                i+=1
        for i in range(len(arr)):
            if arr[i]!=i+1:
                return i+1
        return len(arr)+1
