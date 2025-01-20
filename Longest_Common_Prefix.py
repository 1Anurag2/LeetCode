class Solution:
    def longestCommonPrefix(self, strs:list[str]) ->  str:
        if not strs:
            return ""
        
        # Start with the first string as the prefix
        prefix = strs[0]
        
        for string in strs[1:]:
            # Compare the prefix with each string
            while string[:len(prefix)] != prefix and prefix:
                # Reduce the prefix length by one until a match is found
                prefix = prefix[:len(prefix)-1]
            
            # If the prefix becomes empty, no common prefix exists
            if not prefix:
                return ""
        
        return prefix

solution = Solution()
strs1 = ["flower", "flow", "flight"]
strs2 = ["dog", "racecar", "car"]

print(solution.longestCommonPrefix(strs1))  
print(solution.longestCommonPrefix(strs2))  
