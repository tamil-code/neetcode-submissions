class Solution:
    def jump(self, nums: List[int]) -> int:
        max_reach = 0
        jump_count= 0
        current_end = 0
        for i in range(len(nums)-1):  # when we reach the end no need to compute     
            max_reach = max(max_reach, i + nums[i])
            if i == current_end:
                jump_count+=1
                current_end = max_reach
        return jump_count
