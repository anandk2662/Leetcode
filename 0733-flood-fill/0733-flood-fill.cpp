class Solution {
public:
    void dfs(vector<vector<int>>& image , int i , int j,int n,int m, int orgCol, int newCol){
        if(i<0||j<0||i>=n||j>=m||image[i][j]!=orgCol || image[i][j]==newCol) return;
        image[i][j]=newCol;
        dfs(image,i+1,j,n,m,orgCol,newCol);
        dfs(image,i-1,j,n,m,orgCol,newCol);
        dfs(image,i,j+1,n,m,orgCol,newCol);
        dfs(image,i,j-1,n,m,orgCol,newCol);
    }
    vector<vector<int>> floodFill(vector<vector<int>>& image, int i, int j, int newColor) {
        int n=image.size();
        int m=image[0].size();
        int orgColor=image[i][j];
        dfs(image,i,j,n,m,orgColor,newColor);

        return image;
    }
};