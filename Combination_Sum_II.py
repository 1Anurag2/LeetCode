class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        def backtrack(start, target, path, result):
            if target == 0:
                result.append(path)
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue  # skip duplicates
                
                if candidates[i] > target:
                    break  
                
                backtrack(i + 1, target - candidates[i], path + [candidates[i]], result)
        
        candidates.sort()
        result = []
        backtrack(0, target, [], result)
        return result
