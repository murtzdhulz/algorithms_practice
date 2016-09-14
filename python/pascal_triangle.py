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

ans=Pascal()
triangle= ans.pascal_triangle(5)
for row in triangle:
    print row