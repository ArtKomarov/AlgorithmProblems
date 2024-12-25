import sys
from typing import List

class Solution:
    def calculateBest(self, height: List[int], leftBoundary: int, rightBoundary: int, newLeftBoundary: int, newRightBoundary: int):
        bestLeft = leftBoundary
        bestRight = rightBoundary
        maxArea = self.calculateArea(height, leftBoundary, rightBoundary)

        for l, r in [[leftBoundary, newRightBoundary], [newLeftBoundary, rightBoundary], [newLeftBoundary, newRightBoundary], [leftBoundary, newLeftBoundary], [newRightBoundary, rightBoundary]]:
            area = self.calculateArea(height, l, r)
            if area > maxArea:
                maxArea = area
                bestLeft = l
                bestRight = r

        return maxArea, bestLeft, bestRight


    def maxArea(self, height: List[int]) -> int:
        leftBoundary = 0
        rightBoundary = len(height) - 1
        maxArea = self.calculateArea(height, leftBoundary, rightBoundary)
        
        newLeftBoundary = 1
        newRightBoundary = rightBoundary - 1

        while newLeftBoundary < newRightBoundary:
            if height[newLeftBoundary] <= height[leftBoundary]:
                area = self.calculateArea(height, leftBoundary, newLeftBoundary)
                if area > maxArea:
                    maxArea = area
                newLeftBoundary += 1
                continue

            if height[newRightBoundary] <= height[rightBoundary]:
                area = self.calculateArea(height, newRightBoundary, rightBoundary)
                if area > maxArea:
                    maxArea = area
                newRightBoundary -= 1
                continue
            


            area, bestLeftBoundary, bestRightBoundary = self.calculateBest(height, leftBoundary, rightBoundary, newLeftBoundary, newRightBoundary)
            if area > maxArea:
                maxArea = area

            if bestLeftBoundary == leftBoundary:
                if bestRightBoundary == newRightBoundary:
                    rightBoundary = newRightBoundary
                    newRightBoundary += 1
                elif bestRightBoundary == newLeftBoundary:
                    rightBoundary = newRightBoundary
                    newRightBoundary -= 1
                else: # bestRightBoundary == rightBoundary
                    if newRightBoundary > newLeftBoundary:
                        newLeftBoundary += 1
                    elif newRightBoundary < newLeftBoundary:
                        newRightBoundary -= 1
                    else:
                        newLeftBoundary += 1
                        newRightBoundary -= 1
            elif bestLeftBoundary == newLeftBoundary:
                leftBoundary = newLeftBoundary

                if bestRightBoundary == newRightBoundary:
                    rightBoundary = newRightBoundary
                else:
                    rightBoundary -= 1
            else: # bestLeftBoundary == newRightBoundary
                leftBoundary = newLeftBoundary
                newLeftBoundary += 1

        # Last check
        area, _, _, = self.calculateBest(height, leftBoundary, rightBoundary, newLeftBoundary, newRightBoundary)
        if area > maxArea:
            maxArea = area

        return maxArea
    
    def calculateArea(self, height: List[int], leftBoundary: int, rightBoundary: int) -> int:
        return (rightBoundary - leftBoundary) * min(height[leftBoundary], height[rightBoundary])

    def maxAreaS2(self, height: List[int]) -> int:
        maxArea = self.calculateArea(height, 0, len(height)-1)

        leftBiggest = 0
        leftBiggestHeight = height[0]

        for i1 in range(0, len(height) - 1):
            if height[i1] < leftBiggestHeight:
                area = self.calculateArea(height, leftBiggest, i1)
                if area > maxArea:
                    maxArea = area
                continue
            else:
                leftBiggest = i1
                leftBiggestHeight = height[i1]

            rightBiggestHeight = height[len(height)-1]
            rightBiggest = len(height) - 1
            for i2 in reversed(range(i1 + 1, len(height))):
                if height[i2] < rightBiggestHeight:
                    area = self.calculateArea(height, i2, rightBiggest)
                    if area > maxArea:
                        maxArea = area
                    continue
                else:
                    rightBiggestHeight = height[i2]
                    rightBiggest = i2

                area = min(height[i1], height[i2]) * (i2 - i1)
                if area > maxArea:
                    maxArea = area

        return maxArea



def printCase(heights, sol):
    solution = Solution()
    print(solution.maxAreaS2(heights), sol)

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