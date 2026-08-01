class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        d={}
        s,ans=0,0
        for i in range(len(nums)):
            s+=nums[i]
            if nums[i] in d:
                d[nums[i]]+=1
            else:
                d[nums[i]]=1
            if i>=k:
                s-=nums[i-k]
                d[nums[i-k]]-=1
                if d[nums[i-k]]==0:
                    d.pop(nums[i-k])
            if i>=k-1 and len(d)==k:
                ans=max(ans,s)
        return ans
        
