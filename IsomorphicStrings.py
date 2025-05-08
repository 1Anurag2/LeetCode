from typing import List

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_to_t = {}
        t_to_s = {}

        for cs, ct in zip(s, t):
            if cs in s_to_t:
                if s_to_t[cs] != ct:
                    return False
            else:
                if ct in t_to_s:
                    return False
                s_to_t[cs] = ct
                t_to_s[ct] = cs

        return True
