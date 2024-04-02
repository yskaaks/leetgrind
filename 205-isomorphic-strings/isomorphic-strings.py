class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        map_s_to_t = {}
        map_t_to_s = {}

        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]

            if (char_s in map_s_to_t and map_s_to_t[char_s] != char_t) or (
                char_t in map_t_to_s and map_t_to_s[char_t] != char_s
            ):
                return False
            map_s_to_t[char_s] = char_t
            map_t_to_s[char_t] = char_s
        return True