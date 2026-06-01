class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = {}
        for x in nums:
            if x not in map:
                map[x] = 1
            else: return True
        return False
        