import math as m

class Pascal:
    def pascal_triangle(self,rows):
        triangle=[[1]]
        if rows==1:
            return triangle
        for i in range(1,rows):
            prev=triangle[i-1]
            cur=[prev[0]]
            for j in range(1,len(prev)/2+1):
                cur_sum=prev[j-1]+prev[j]
                cur.append(cur_sum)
            temp=list(cur)
            temp.reverse()
            cur.extend(temp)
            if (i+1)%2==1:
                cur.pop(len(cur)/2)
            triangle.append(cur)
        return triangle

    # x,y are index positions -> row,column index
    def pascal_entry_recursive(self,x,y):
        if x+1==1 or y+1==1 or x==y:
            return 1
        return self.pascal_entry_recursive(x-1,y-1)+self.pascal_entry_recursive(x-1,y)

    # C(n,k+1) = C(n,k) * (n-k) / (k+1)
    # Index value = n (0 indexed)
    def pascal_triangle_row(self,n):
        L=[1]
        for i in range(n):
            # print L,i,n
            L.append(L[i]*(n-i)/(i+1))
        return L

ans=Pascal()
# triangle= ans.pascal_triangle(5)
# for row in triangle:
#     print row
print ans.pascal_entry_recursive(3,2) # --> 3
print ans.pascal_triangle_row(3)