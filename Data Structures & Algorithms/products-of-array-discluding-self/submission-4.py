class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, postfix = [1]*len(nums), [1]*len(nums)

        for index, value in enumerate(nums):
            if index == 0:
                continue
            prefix[index] = prefix[index-1] * nums[index-1]
        print(prefix)
        res = [1] * len(nums)
        for index, value in reversed(list(enumerate(nums))):   
            if(index == len(nums) - 1):
                continue
            postfix[index] = postfix[index+1]* nums[index+1]
        print(postfix)
        for index, value in enumerate(res):
            res[index] = prefix[index] * postfix[index]
        
        return res



        