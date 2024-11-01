
// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
  public:
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2) {
        ListNode *result = new ListNode();
        int additionalTerm = 0;

        // First iteration
        result->val = l1->val + l2->val;
        additionalTerm = result->val / 10;
        result->val %= 10;

        ListNode *l1Pointer = l1->next;
        ListNode *l2Pointer = l2->next;
        ListNode *beforeResultPointer = result;

        while (l1Pointer != nullptr && l2Pointer != nullptr) {
            beforeResultPointer->next =
                new ListNode(l1Pointer->val + l2Pointer->val + additionalTerm);

            beforeResultPointer = beforeResultPointer->next;

            additionalTerm = beforeResultPointer->val / 10;
            beforeResultPointer->val %= 10;

            l1Pointer = l1Pointer->next;
            l2Pointer = l2Pointer->next;
        }

        // Leftovers from l1
        while (l1Pointer != nullptr) {
            beforeResultPointer->next =
                new ListNode(l1Pointer->val + additionalTerm);

            beforeResultPointer = beforeResultPointer->next;

            additionalTerm = beforeResultPointer->val / 10;
            beforeResultPointer->val %= 10;

            l1Pointer = l1Pointer->next;
        }

        // Leftovers from l2
        while (l2Pointer != nullptr) {
            beforeResultPointer->next =
                new ListNode(l2Pointer->val + additionalTerm);

            beforeResultPointer = beforeResultPointer->next;

            additionalTerm = beforeResultPointer->val / 10;
            beforeResultPointer->val %= 10;

            l2Pointer = l2Pointer->next;
        }

        // Leftover if len(l1) == len(l2)
        if (additionalTerm != 0) {
            beforeResultPointer->next = new ListNode(additionalTerm);
        }

        return result;
    }
};