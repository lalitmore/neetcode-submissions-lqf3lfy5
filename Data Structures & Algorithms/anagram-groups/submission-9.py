class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            arr = [0] * 26
            for char in word:
                arr[ord(char)-97] += 1
            res[tuple(arr)].append(word)
        return list(res.values())
            
                
        