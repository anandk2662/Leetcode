class Solution {
public:
    int maxArea(vector<int>& height) {
        int maxWater=0;
        int lb=0,rb=height.size()-1;
        while(lb<rb){
            int w=rb-lb;
            int h=min(height[lb],height[rb]);
            int currWater=w*h;
            maxWater=max(maxWater,currWater);
            height[lb]>height[rb]?rb-- : lb++;
        }
        return maxWater;
    }
};