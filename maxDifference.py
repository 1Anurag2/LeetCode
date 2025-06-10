from collections import Counter

class Solution:
    def maxDifference(self, s: str) -> int:
        freq = Counter(s)
        max_diff = float('-inf')
        found = False

        # Get all characters with odd and even frequencies
        odd_freqs = [v for v in freq.values() if v % 2 == 1]
        even_freqs = [v for v in freq.values() if v % 2 == 0]

        for odd in odd_freqs:
            for even in even_freqs:
                diff = odd - even
                max_diff = max(max_diff, diff)
                found = True

        return max_diff if found else 0
