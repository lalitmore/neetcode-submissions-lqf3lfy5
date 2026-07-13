class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]*len(nums)
        for index, value in enumerate(nums):
            if index == 0: continue
            else:
                prefix[index] = prefix[index-1]*nums[index-1]
        print("prefix: ", prefix)

        postfix = [1]*len(nums)
        for index, value in reversed(list(enumerate(nums))):
            if index == len(nums) - 1: continue
            else:
                postfix[index] = postfix[index + 1] * nums[index + 1]
        
        res = [0]*len(nums)
        for index, value in enumerate(prefix):
            res[index] = value * postfix[index]
        return res




        