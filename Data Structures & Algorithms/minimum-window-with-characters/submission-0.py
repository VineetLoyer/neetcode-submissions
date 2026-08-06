class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Base case: If t is longer than s, it's impossible
        if not s or not t or len(t) > len(s):
            return ""
        
        # Frequency map for characters in t
        target_count = Counter(t)
        # Dictionary to keep track of characters in the current window
        window_count = {}
        
        # Two pointers and other variables
        start, end = 0, 0
        min_len = float('inf')
        min_window = ""
        have, need = 0, len(target_count)
        
        # Sliding window approach
        while end < len(s):
            # Add the current character to the window
            char = s[end]
            window_count[char] = window_count.get(char, 0) + 1
            
            # Check if we have enough of this character
            if char in target_count and window_count[char] == target_count[char]:
                have += 1
            
            # Try to contract the window when all characters are found
            while have == need:
                # Update the smallest window
                if (end - start + 1) < min_len:
                    min_len = end - start + 1
                    min_window = s[start:end+1]
                
                # Remove the start character from the window
                start_char = s[start]
                window_count[start_char] -= 1
                if start_char in target_count and window_count[start_char] < target_count[start_char]:
                    have -= 1
                start += 1
            
            # Expand the window
            end += 1
        
        return min_window