class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, postfix = [0]*len(nums),[0]*len(nums)
        for index, value in enumerate(nums):
            if index == 0:
                prefix[0] = 1
            else:
                prefix[index] = nums[index-1]*prefix[index-1]
        for index, value in reversed(list(enumerate(nums))):
            if index == (len(nums) - 1):
                postfix[index] = 1
            else:
                postfix[index] = nums[index + 1]*postfix[index+1]


        print("Prefix: ", prefix)
        print("Postfix: ", postfix)
        res = [0] * len(nums)
        for index,value in enumerate(prefix):
            res[index] = postfix[index]*value
        return res
        




        