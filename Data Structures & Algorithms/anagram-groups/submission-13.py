class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for index, word in enumerate(strs):
            array = [0]*26
            for index, char in enumerate(word):
                array[ord(char) - ord('a')] += 1
            if tuple(array) in res:
                res[tuple(array)] += [word]
            else:
                res[tuple(array)] = [word]
        print("res: ", res)
        return list(res.values())



            
            
            
                
        