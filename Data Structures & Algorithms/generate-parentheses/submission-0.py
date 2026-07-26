class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        def isValid(s: str) -> bool:
            stack = []
            mapping = {')': '(', ']': '[', '}': '{'}
            for ch in s:
                if ch in mapping.values():  # opening bracket
                    stack.append(ch)
                elif ch in mapping:         # closing bracket
                    if not stack or stack[-1] != mapping[ch]:
                        return False
                    stack.pop()
                else:
                    # ignore invalid characters (optional)
                    return False
            return True
        def compute(brackets,op,cl,n,res):
            if op==n and cl==n:
                if isValid(brackets):
                    res.append(brackets)
            if op<n:
                compute(brackets + "(", op+1,cl,n,res)
            if cl<n:
                compute(brackets + ")", op,cl+1,n,res)
        res=[]
        compute("",0,0,n,res)
        return res