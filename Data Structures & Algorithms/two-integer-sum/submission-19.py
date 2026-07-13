class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for index, value in enumerate(nums):
            diff = target-value
            print("Hashmap: ", hash_map)
            print("Diff: ", diff)
            if diff in hash_map:
                return [hash_map[diff], index]
            else: hash_map[value] = index
        
        return []