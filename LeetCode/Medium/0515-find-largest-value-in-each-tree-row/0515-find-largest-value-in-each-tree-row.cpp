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
    vector<int> largestValues(TreeNode* root) {
        if (!root) return {};

        deque<TreeNode*> q;
        vector<int> ans;
        q.push_back(root);
        while(!q.empty()){
            int max_val = INT_MIN;
            int size = q.size();
            for(int i = 0; i < size; i++){
                TreeNode* cur = q.front();
                q.pop_front();
                max_val = max(max_val, cur->val);
                if (cur->left) q.push_back(cur->left); 
                if (cur->right) q.push_back(cur->right);  //
            }
            ans.push_back(max_val);
        }
        return ans;
    }
};