class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_dict=defaultdict(list)
        for s in strs:
            sorteds=''.join(sorted(s))
            ana_dict[sorteds].append(s)
        return list(ana_dict.values())
    
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     result = []  # To store the grouped anagrams
    #     used = [False] * len(strs)  # To keep track of which strings have been grouped
    
    #     for i in range(len(strs)):
    #         if not used[i]:  # If the string is not already grouped
    #             group = [strs[i]]  # Start a new group with the current string
    #             used[i] = True
    #             for j in range(i + 1, len(strs)):
    #                 if not used[j] and are_anagrams(strs[i], strs[j]):
    #                     group.append(strs[j])
    #                     used[j] = True
    #             result.append(group)
        
    #     return result
    # def are_anagrams(s1, s2):
    #     return sorted(s1) == sorted(s2)