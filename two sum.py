class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        s=[]
        for i in range(len(nums)-1):
            j=i+1
            while(j<len(nums)):
                if nums[i] + nums[j]==target:
                    s.append(i)
                    s.append(j)
                    return s
                j+=1
        print(s)
q=Solution()
w=[2,7,11,15]
t = 9
q.twoSum(w,t)