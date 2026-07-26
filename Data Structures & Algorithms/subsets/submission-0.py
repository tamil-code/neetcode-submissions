class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        def generateSubsets(p:List[int],up:List[int]):
            if len(up)==0:
                result.append(p)
                return
            generateSubsets(p+[up[0]],up[1:])
            generateSubsets(p,up[1:])
        generateSubsets([],nums)
        return result