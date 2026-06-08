class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = Counter(nums);
        print(frequency)
        res = []
        ans = 1
        # Sorts descending (highest score to lowest)
        for key, value in sorted(frequency.items(), key=lambda item: item[1], reverse=True):
            print(key,value)
            while ans <= k and key not in res:
                res.append(key)
                ans += 1
        return res