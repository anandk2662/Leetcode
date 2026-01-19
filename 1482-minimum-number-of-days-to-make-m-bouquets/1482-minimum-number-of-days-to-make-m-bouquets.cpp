class Solution {
public:
    int Possible(vector<int>b,int d,int k){
        int count=0;
        int noOfBloom=0;
        for(int i=0;i<b.size();i++){
            if (b[i]<=d){
                count++;
            }else{
                noOfBloom+=(count/k);
                count=0;
            }
            
        }
        noOfBloom+=(count/k);
        return noOfBloom;

    }
    int minDays(vector<int>& bloomDay, int m, int k) {
        if ((long long)m*k>bloomDay.size()){
            return -1;
        }
        int low=*min_element(bloomDay.begin(), bloomDay.end());
        int high=*max_element(bloomDay.begin(), bloomDay.end());
        int ans=high;
        while(low<=high){
            int mid=(low+high)>>1;
            if (Possible(bloomDay,mid,k)>=m){
                ans=mid;
                high=mid-1;
            }else{
                low=mid+1;
            }
        }
        return ans;
    }
};