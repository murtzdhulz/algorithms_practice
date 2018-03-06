class Solution(object):
    def spiralOrderSimulation(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # This is the simulation solution
        if not matrix: return []
        ans= []
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        R, C = len(matrix), len(matrix[0])
        seen = [[False]*len(matrix[0]) for _ in matrix]
        r=c=di=0
        for _ in xrange(R*C):
            ans.append(matrix[r][c])
            seen[r][c]=True
            cr, cc = r+dr[di], c+dc[di]
            if 0<=cr<R and 0<=cc<C and not seen[cr][cc]:
                r,c=cr,cc
            else:
                di=(di+1)%4
                r,c = r+dr[di], c+dc[di]
        return ans

    def spiralOrderLayered(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        def get_coords(r1, r2, c1, c2):
            for c in xrange(c1, c2 + 1):
                yield r1, c
            for r in xrange(r1 + 1, r2 + 1):
                yield r, c2
            if c1 < c2 and r1 < r2:
                for c in xrange(c2 - 1, c1 - 1, -1):
                    yield r2, c
                for r in xrange(r2 - 1, r1, -1):
                    yield r, c1

        # This is the layered solution
        if not matrix: return []
        ans = []
        r1, r2 = 0, len(matrix) - 1
        c1, c2 = 0, len(matrix[0]) - 1
        while r1 <= r2 and c1 <= c2:
            for r, c in get_coords(r1, r2, c1, c2):
                ans.append(matrix[r][c])
            r1 += 1;
            r2 -= 1;
            c1 += 1;
            c2 -= 1
        return ans

"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
"""