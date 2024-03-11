class Solution:
    def customSortString(self, order: str, s: str) -> str:
        s_map = collections.Counter(s)
        print(s_map)
        res = []
        for char in order:
            if char in s_map:
                res.append(char)
                s_map[char] -= 1
                if s_map[char] != 0:
                    for i in range(s_map[char]):
                        res.append(char)
                        s_map[char] -= 1
            if s_map[char] == 0:
                del s_map[char]
        
        for char in s_map:
            for i in range(s_map[char]):
                res.append(char)
                s_map[char] -= 1
        return "".join(res)