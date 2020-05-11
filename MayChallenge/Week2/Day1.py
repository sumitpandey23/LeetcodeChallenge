"""
Check If It Is a Straight Line

You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.
 
Example 1:



Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true
Example 2:



Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false
 

Constraints:

2 <= coordinates.length <= 1000
coordinates[i].length == 2
-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
coordinates contains no duplicate point.

"""

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        i, j = coordinates[:2]
        return all(i[0] * j[1] - j[0] * i[1] +
                   j[0] * k[1] - k[0] * j[1] +
                   k[0] * i[1] - i[0] * k[1] == 0
                   for k in coordinates)
