class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        nums.sort()
        for x in nums:
            if x in frequency:
                frequency[x] += 1
            else:
                frequency[x] = 1
        
        res = [0] * k

        top_k_dict = dict(sorted(frequency.items(), key=lambda x: x[1], reverse=True)[:k])
        return list(top_k_dict.keys())

        for key, value in frequency.items():
            print(f"Key: {key}, Value: {value}")