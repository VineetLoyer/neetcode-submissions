class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_dict=defaultdict(list)
        for s in strs:
            sorteds=''.join(sorted(s))
            ana_dict[sorteds].append(s)
        return list(ana_dict.values())