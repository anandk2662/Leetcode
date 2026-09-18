class Solution {
public:
    long long calculateHours(vector<int>& piles,int k){
        long long hours=0;
        for(int i=0;i<piles.size();i++){
            hours+=ceil((double)piles[i]/k);
        }
        return hours;
    }
    int minEatingSpeed(vector<int>& piles, int h) {
        int st=1,end =* max_element(piles.begin(),piles.end());
        int ans;
        while(st<=end){
            int mid=st+(end-st)/2;
            long long reqHours=calculateHours(piles,mid);
            if(reqHours<=h){
                ans=mid;
                end=mid-1;
            }else{
                st=mid+1;
            }
        }

        return ans;
    }
};