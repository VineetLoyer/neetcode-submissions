class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]

        match_expr = {'(':')','{':'}','[':']'}

        for char in s:
            if char in '({[':
                stack.append(char)
            elif char in ')}]':
                if not stack or (match_expr[stack[-1]] != char):
                    return False
                stack.pop()
        return len(stack)==0