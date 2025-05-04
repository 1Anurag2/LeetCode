from collections import Counter
from typing import List

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = 0
        sorted_dominoes = [tuple(sorted(domino)) for domino in dominoes]

        count_domino = Counter(sorted_dominoes)

        for freq in count_domino.values():
            count += freq*(freq-1) // 2
        return count