class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result =[]
        def backtrack(current:str,open_c:int,close_c:int):
            if len(current)==2*n:
                result.append(current)
            
            if open_c<n:
                backtrack(current +"(",open_c+1,close_c)
            if close_c<open_c:
                backtrack(current+")",open_c,close_c+1)
        backtrack("",0,0)
        return result
    