class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix #put each prefix in pos in
            prefix *=  nums[i] 
        postfix = 1
        for i in range(len(nums) -1, -1, -1): #start,#stop,step
            res[i] *= postfix
            postfix *= nums[i]
        return res


