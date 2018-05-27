class Solution(object):
    def numMagicSquaresInside_v1(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        def check_cur_square(r, c):
            if r + 2 >= len(grid) or c + 2 >= len(grid):
                return False
            rows = [0] * 3
            cols = [0] * 3
            diag = [0] * 2

            # check distinct and less than 10
            distinct = set()
            for i in xrange(3):
                for j in xrange(3):
                    if grid[i + r][j + c] > 9 or grid[i + r][j + c] == 0:
                        return False
                    if grid[i + r][j + c] in distinct:
                        return False
                    distinct.add(grid[i + r][j + c])

            for i in xrange(3):
                for j in xrange(3):
                    rows[i] += grid[i + r][j + c]
                    cols[j] += grid[i + r][j + c]

            for i in xrange(3):
                diag[0] += grid[i + r][i + c]
                diag[1] += grid[i + r][c + (2 - i)]

            one_val = rows[0]
            for val in rows + cols + diag:
                if val != one_val:
                    return False
            return True

        res = 0
        for r1 in xrange(len(grid)):
            for c1 in xrange(len(grid[0])):
                if check_cur_square(r1, c1):
                    res += 1
        return res

    def numMagicSquaresInside_v2(self, grid):
        R, C = len(grid), len(grid[0])

        def magic(a,b,c,d,e,f,g,h,i):
            return (sorted([a,b,c,d,e,f,g,h,i]) == range(1, 10) and
                (a+b+c == d+e+f == g+h+i == a+d+g ==
                 b+e+h == c+f+i == a+e+i == c+e+g == 15))

        ans = 0
        for r in xrange(R-2):
            for c in xrange(C-2):
                if magic(grid[r][c], grid[r][c+1], grid[r][c+2],
                         grid[r+1][c], grid[r+1][c+1], grid[r+1][c+2],
                         grid[r+2][c], grid[r+2][c+1], grid[r+2][c+2]):
                    ans += 1
        return ans

"""
A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.

Given an grid of integers, how many 3 x 3 "magic square" subgrids are there?  (Each subgrid is contiguous).

 

Example 1:

Input: [[4,3,8,4],
        [9,5,1,9],
        [2,7,6,2]]
Output: 1
Explanation: 
The following subgrid is a 3 x 3 magic square:
438
951
276

while this one is not:
384
519
762

In total, there is only one magic square inside the given grid.
"""

