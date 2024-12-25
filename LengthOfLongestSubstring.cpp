#include <iostream>
#include <string>

int lengthOfLongestSubstring(std::string &s) {
    if (s.length() == 0) {
        return 0;
    }

    size_t startIndex = 0;
    size_t lastIndex = 0;

    size_t maxLen = 1;

    for (size_t i = 1; i < s.length(); ++i) {
        lastIndex++;
        auto startIter = s.begin() + static_cast<long>(startIndex);
        auto lastIter = s.begin() + static_cast<long>(lastIndex);

        auto found = std::find(startIter, lastIter, s[i]);
        if (found == lastIter) {
            if (lastIndex - startIndex + 1 > maxLen) {
                maxLen = lastIndex - startIndex + 1;
            }
        } else {
            startIndex += static_cast<size_t>(found - startIter) + 1;
        }
    }

    return static_cast<int>(maxLen);
}

int main() {
    std::string s("abcbbbbbcdebb");
    std::cout << lengthOfLongestSubstring(s) << std::endl;
    return 0;
}