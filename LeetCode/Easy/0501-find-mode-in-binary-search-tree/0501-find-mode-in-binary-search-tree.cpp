/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> findMode(TreeNode* root) {
        map<int, int> count;
        TreeNode* cur;
        queue<TreeNode*> q;
        q.push(root);
        while(!q.empty()){
            cur = q.front();
            q.pop();
            count[cur->val]++;

            if(cur->left)
                q.push(cur->left);
            if(cur->right)
                q.push(cur->right);
        }

        int max_cnt = 0;
        for(auto &pair : count){
            max_cnt = max(max_cnt, pair.second);
        }

        vector<int> ans;
        for(auto &pair : count){
            if(pair.second == max_cnt)
                ans.push_back(pair.first);
        }
        return ans;
    }
};