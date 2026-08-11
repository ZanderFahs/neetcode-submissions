class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        for i in range(len(strs)):
            subset = []
            subset.append(strs[i])
            for j in range(len(strs)):
                if i != j:
                    if sorted(strs[i]) == sorted(strs[j]):
                        subset.append(strs[j])
            subset.sort()            
            if subset not in output:
                output.append(subset)
        
        return output

        

