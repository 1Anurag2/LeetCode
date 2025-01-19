class Solution:
    def romanToInt(self, s: str) -> int:
        
        roman_to_int_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        
        total = 0
        prev_value = 0

        for symbol in reversed(s):
            value = roman_to_int_map[symbol]
            
            # Check if we need to subtract or add the value
            if value < prev_value:
                total -= value
            else:
                total += value
            
            # Update previous value for the next iteration
            prev_value = value
        
        return total

# Example usage:
solution = Solution()
print(solution.romanToInt("III"))    
print(solution.romanToInt("LVIII"))  
print(solution.romanToInt("MCMXCIV"))
