class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        words = set(wordDict)
        if not words: #empty wordDict
            return False
        minLen = min(map(len,words))
        maxLen = max(map(len,words))

        dp = [False]*(n+1)
        dp[0] = True # empty string is segmentable

        for i in range(1,n+1):
            for L in range(minLen,maxLen+1):
                j = i-L
                if j>=0 and dp[j] and s[j:i] in words:
                    dp[i] = True
                    break
        return dp[n]