__author__ = 'Murtaza'

def cut_rod(price,n):
    val = [0]

    for i in range(0,n):
        max_val = float('-inf')
        for j in range(i+1):
            max_val = max(max_val,price[j]+val[i-j])
        val.append(max_val)

    return val


# Driver program to test above functions
arr = [1, 5, 8, 9, 10, 17, 17, 20]
size = len(arr)
print("Maximum Obtainable Value is " + str(cut_rod(arr, size)))