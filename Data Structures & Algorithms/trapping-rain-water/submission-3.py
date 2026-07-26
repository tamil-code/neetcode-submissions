class Solution:
    def trap(self, height: List[int]) -> int:
        left,right=0,len(height)-1
        maxL, maxR = height[left] , height[right]
        res=0
        while(left<right):
            if(height[left] <= height[right]):
                left+=1
                if height[left] > maxL:
                    maxL = height[left]
                vol = maxL - height[left]
                if(vol>0):res+=vol
            else:
                right-=1
                if height[right] > maxR:
                    maxR = height[right]
                vol = maxR - height[right]
                if(vol>0):res+=vol
            

        return res