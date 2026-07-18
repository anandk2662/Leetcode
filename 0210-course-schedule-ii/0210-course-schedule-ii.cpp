class Solution {
public:
    bool isCycle(int src,vector<bool>& vis, vector<vector<int>> &adj,vector<bool>& recPath){
        vis[src]=true;
        recPath[src]=true;
        for (int v:adj[src]){
                if(!vis[v]){

                    if(isCycle(v,vis,adj,recPath)) return true;
                }
                else if (recPath[v]) {
                    return true;
            }
        }
        recPath[src]=false;
        return false;
        }
    void  toposort(int src,vector<bool>& vis, vector<vector<int>> &adj, stack<int> &s){
        vis[src]=true;

        for (int v:adj[src]){
                if(!vis[v]){
                    toposort(v,vis,adj,s);
                }
            }
            s.push(src);
        }

    vector<int> findOrder(int n, vector<vector<int>>& edges) {
        vector<bool> vis(n,false);
        vector<bool> recPath(n,false);

        vector<int> ans;
        stack<int> s;

        //adjecency list
        vector<vector<int>>adj(n);

        for (auto &e: edges){
            int v=e[0];
            int u=e[1];

            adj[u].push_back(v);
        }
        //check cycle

        for (int i=0;i<n;i++){
            if(!vis[i]){
                if(isCycle(i,vis,adj,recPath)) return ans;
            }
        }

        vis.assign(n,false);
        for (int i=0;i<n;i++){
            if(!vis[i]){
                toposort(i,vis,adj,s);
            }
        }

        while(!s.empty()) {
            ans.push_back(s.top());
            s.pop();
    }

    return ans;
    }
};