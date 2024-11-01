#include <iostream>
#include <unordered_map>
#include <vector>

std::vector<int> twoSum(std::vector<int> &nums, int target) {
    std::vector<int> copy = nums;
    std::unordered_map<int, int> map;

    for (size_t i = 0; i < nums.size(); ++i) {
        auto found = map.find(nums[i]);
        if (found != map.end()) {
            return std::vector<int>{static_cast<int>(i), found->second};
        }
        map[target - nums[i]] = static_cast<int>(i);
    }

    std::cout << "Solution not found" << std::endl;
    return std::vector<int>{};
}

int main() {
    std::vector<int> example{0, 3, -3, 4, -1};
    int target = -1;

    std::vector<int> res = twoSum(example, target);

    std::cout << res[0] << " " << res[1] << std::endl;

    return 0;
}
