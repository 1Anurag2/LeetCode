class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        # Sort words based on the number at the end
        words.sort(key=lambda word: int(word[-1]))
        # Remove the numbers and join the words
        return ' '.join(word[:-1] for word in words)
