class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_map = {}
        for index, x in enumerate(nums):
            #my_map[x] = index
            difference = target - x
            if(difference in my_map):
                return [my_map.get(difference), index]
            else:
                my_map[x] = index
        return []
