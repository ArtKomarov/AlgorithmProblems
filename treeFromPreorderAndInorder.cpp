#include <iostream>
#include <stack>

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right)
        : val(x), left(left), right(right) {}
};

class Solution {
  public:
    TreeNode *buildTree(std::vector<int> &preorder, std::vector<int> &inorder) {
        std::stack<int> lastNode;
        TreeNode *node = new TreeNode(preorder[0]);
        lastNode.push(preorder[0]);
        int currentNode = preorder[0];

        for (size_t i = 0; i < preorder.size(); ++i) {
            if (currentNode == inorder[i]) {
            }
        }
        return node;
    }
};

int main() {
    std::cout << "Hello" << std::endl;
    return 0;
}