import sys
from typing import List

class Solution:
    def calculateArea(self, height: List[int], left_boundary: int, right_boundary: int) -> int:
        return (right_boundary - left_boundary) * min(height[left_boundary], height[right_boundary])
    
    def maxArea(self, height: List[int]) -> int:
        left_boundary = 0
        right_boundary = len(height) - 1
        maxArea = 0
        while left_boundary < right_boundary:
            area = self.calculateArea(height, left_boundary, right_boundary)
            if area > maxArea:
                maxArea = area

            if height[left_boundary] > height[right_boundary]:
                right_boundary -= 1
            elif height[left_boundary] < height[right_boundary]:
                left_boundary += 1
            else:
                left_boundary += 1
                right_boundary -= 1

        return maxArea


def printCase(heights, sol):
    solution = Solution()
    print(solution.maxArea(heights), sol)

def main() -> int:
    printCase([10,14,10,4,10,2,6,1,6,12], 96)

    printCase([1,8,6,2,5,4,8,3,7], 49)
    printCase([1,2], 1)
    printCase([8,7,2,1], 7)
    printCase([2,3,10,5,7,8,9], 36)
    printCase([10,14,10,4,10,2,6,1,6,12], 96)
    printCase([76,155,15,188,180,154,84,34,187,142,22,5,27,183,111,128,50,58,2,112,179,2,100,111,115,76,134,120,118,103,31,146,58,198,134,38,104,170,25,92,112,199,49,140,135,160,20,185,171,23,98,150,177,198,61,92,26,147,164,144,51,196,42,109,194,177,100,99,99,125,143,12,76,192,152,11,152,124,197,123,147,95,73,124,45,86,168,24,34,133,120,85,81,163,146,75,92,198,126,191], 18048)

    return 0

if __name__ == '__main__':
    sys.exit(main())