class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=set()
        candidates.sort()
        def dfs(i:int,curr:List[int],total:int):
            if total==target:
                res.add(tuple(curr))
                return
            if i>len(candidates)-1 or total>target:
                return
            curr.append(candidates[i])
            dfs(i+1,curr,total+candidates[i])
            curr.pop()
            dfs(i+1,curr,total)
        dfs(0,[],0)
        return [list(combination) for combination in res]