class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for x in s:
            if x == "(" or x == "[" or x == "{":
                st.append(x)
            else:
                if len(st) ==0:
                    return False
                curr = st.pop()
                par=x
                match par:
                    case  ")":
                        if (curr != "("): return False
                    case "]":
                        if (curr != "["): return False
                    case  "}":
                        if (curr != "{"): return False
                    
        return len(st) == 0
                    
        