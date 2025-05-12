from itertools import permutations
from typing import List
class Solution:
        def findEvenNumbers(self, digits: List[int]) -> List[int]:
                list = []
                for t in set(permutations(digits,3)):
                        s = int(''.join(str(x) for x in t))
                        if(s > 99 and s < 1000):
                                if ( s % 2 == 0):
                                        list.append(s)
                                        # print(list)
                return sorted(list)
sol = Solution()
digits = [2,1,3,0]
sol.findEvenNumbers(digits)