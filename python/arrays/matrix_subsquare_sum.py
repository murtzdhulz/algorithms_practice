__author__ = 'Murtaza'

class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if len(matrix)==0 or len(matrix[0])==0: return
        self.m=len(matrix)
        self.n=len(matrix[0])
        self.nums=[[0]*self.n for _ in xrange(self.m)]
        self.tree=[[0]*(self.n+1) for _ in xrange(self.m+1)]

        for i in xrange(self.m):
            for j in xrange(self.n):
                self.update(i,j,matrix[i][j])


    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        if self.m==0 or self.n==0: return
        delta=val-self.nums[row][col]
        self.nums[row][col]=val

        # we will add delta to row+1,j+1 and all the ancestors
        i,j=row+1,col+1
        while i<=self.m:
            j=col+1
            while j<=self.n:
                self.tree[i][j]+=delta
                j+=j&-j
            i+=i&-i


    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if self.m==0 or self.n==0: return
        return self.sum(row1,col1)+self.sum(row2+1,col2+1)-self.sum(row1,col2+1)-self.sum(row2+1,col1)

    def sum(self, row, col):
        # here we have already taken care of adding 1
        sum=0
        col_start=col
        while row>0:
            col=col_start
            while col>0:
                sum+=self.tree[row][col]
                col-=col&-col
            row-=row&-row
        return sum

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)