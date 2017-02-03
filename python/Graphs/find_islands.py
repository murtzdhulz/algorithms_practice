__author__ = 'Murtaza'

def return_islands(mat):
    res=[]

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j]==0:
                res.append(compute_size(mat,i,j))

    return res

def compute_size(mat,r,c):
    # check bounds and if this cell has already been visited
    if r<0 or c<0 or r>=len(mat) or c>=len(mat[0]) or mat[r][c]!=0:
        return 0

    mat[r][c]=-1
    size=1
    for i in range(-1,2):
        for j in range(-1,2):
          size+=compute_size(mat,r+i,c+j)
    return size

terrain=[[0,1,2,1],[0,0,1,0],[0,2,2,1],[2,3,0,0]]
print return_islands(terrain)