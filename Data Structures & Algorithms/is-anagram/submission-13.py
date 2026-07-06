class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {}
        for x in s:
            if x in s_map:
                s_map[x] = s_map.get(x) + 1
            else:
                s_map[x] = 1

        t_map = {}
        for x in t:
            if x in t_map:
                t_map[x] = t_map.get(x) + 1
            else:
                t_map[x] = 1
        print("S Map: ", s_map)
        print("T Map: ", t_map)
        if s_map == t_map:
            return True
        else: return False
        
        
        
        