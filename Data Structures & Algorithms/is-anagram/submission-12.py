class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        map1 = {}
        for x in s:
            if x not in map1:
                map1[x] = 1
            else:
                map1[x] = 1 + map1.get(x)
        print(map1)
        map2 = {}
        for y in t:
            if y not in map2:
                map2[y] = 1
            else:
                map2[y] = 1 + map2.get(y)
        if map1 == map2:
            return True
        return False