class Solution {
public:
    int binSearch(vector<int>& a, int target,int st , int end){
        if(st<=end){
            int mid=st+(end-st)/2;
            if(target==a[mid]){
                return mid;
            }
            else if (a[mid]<=target){
                return binSearch(a,target ,mid+1,end);
            }else{
                return binSearch(a,target, st,mid-1);
            }
        }
        return -1;
    }
    
    int search(vector<int>& a, int target) {
       return binSearch(a,target,0,a.size()-1);
    }
};