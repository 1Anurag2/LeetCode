class Solution:
    def letterCombinations(self, digits: str):
        if not digits:
            return []

        # Mapping of digits to corresponding letters
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        # Recursive function to generate combinations
        def backtrack(index, current_combination):
            if index == len(digits):
                combinations.append("".join(current_combination))
                return
            
            # Get the letters corresponding to the current digit
            letters = phone_map[digits[index]]
            for letter in letters:
                current_combination.append(letter)
                backtrack(index + 1, current_combination)
                current_combination.pop()  

        combinations = []
        backtrack(0, [])
        return combinations

solution = Solution()
print(solution.letterCombinations("23")) 
print(solution.letterCombinations(""))    
print(solution.letterCombinations("2"))   
