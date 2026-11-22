class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans=[]
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
              sum=nums[i]+nums[j]

              if (sum==target):
                return [i,j]
        return ans
            
