class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        if t == 0:
            return len(s)
        new_string = ''
        for value in s:
            if value == 'z':
                new_string += 'ab'
            else:
                new_string += chr(ord(value)+1)
        # print(new_string)
        return self.lengthAfterTransformations(new_string,t-1) 

sol = Solution()
s = "abcyz"
t = 2
print(sol.lengthAfterTransformations(s,t))