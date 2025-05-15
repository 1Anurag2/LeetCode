from typing import List
class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        list = []
        for i in range(len(groups)-1):
            if groups[i] == groups[i+1]:
                list.append(words[i])
            else:
                list.append(words[i+1])
        return list

sol = Solution()
words = ["e","a","b"]
groups = [0,0,1]
words1 = ["a","b","c","d"]
groups1 = [1,0,1,1]
words2 = ["tu","rv","bn"]
groups2 = [0,0,0]
print(sol.getLongestSubsequence(words,groups))
print(sol.getLongestSubsequence(words1,groups1))
print(sol.getLongestSubsequence(words2,groups2))