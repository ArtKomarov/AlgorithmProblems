#include <iostream>
#include <vector>


struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
    ListNode(std::vector<int>& vec) {
        val = vec[0];
        ListNode* toInit = this;
        for (size_t i = 1; i < vec.size(); ++i) {
            toInit->next = new ListNode(vec[i]);
            toInit = toInit->next;
        }
    }

    friend std::ostream& operator <<(std::ostream& os, const ListNode& node) {
        os << node.val;
        if (node.next != nullptr) {
            os << " " << *node.next;
        }

        return os;
    }
};
 
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        if (head == nullptr) {
            return nullptr;
        }
        ListNode* odd = head;
        ListNode* even = head->next;
        ListNode* newHead = even != nullptr ? even : odd;
        
        while (even != nullptr) {
            ListNode* next = even->next;

            even->next = odd;

            if (next != nullptr) {
                if (next->next != nullptr) {
                    odd->next = next->next;
                } else {
                    odd->next = next;
                }
                even = next->next;
            } else {
                odd->next = nullptr;
                even = nullptr;
            }
            odd = next;
        }

        return newHead;
    }
};

int main() {
    std::vector<int> vals = {1, 2};

    Solution sol;

    ListNode list(vals);
    std::cout << list << std::endl;

    ListNode* newHead = sol.swapPairs(&list);
    std::cout << *newHead << std::endl;

}