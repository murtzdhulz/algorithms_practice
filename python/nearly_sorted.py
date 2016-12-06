__author__ = 'Murtaza'

def sort_k_wiggled(arr,k):
    num_grps = len(arr)/k
    # flag=False
    if len(arr)%k!=0:
        num_grps+=1

    i=1
    while i<num_grps:
        try:
            elements=arr[(i-1)*k:(i+1)*k]
            elements.sort()
            arr[(i-1)*k:(i+1)*k] = elements
        except:
            print "And exception did occur with:",num_grps #Not needed in Python. Can also be handled with a for loop
            elements=arr[(i-1)*k:]
            elements.sort()
            arr[(i-1)*k:] = elements
        i+=1

    # if flag:
    #     elements=arr[num_grps*k:]
    #     elements.sort()
    #     arr[num_grps*k:]=elements
    return arr

def sort_k_wiggled_better(arr,k):
    num_grps = len(arr)/k
    # flag=False
    if len(arr)%k!=0:
        num_grps+=1

    i=1
    while i<num_grps:
        if (i+1)*k>len(arr):
            print "Entered the if:",i
            elements=arr[(i-1)*k:]
            elements.sort()
            arr[(i-1)*k:] = elements
        else:
            elements=arr[(i-1)*k:(i+1)*k]
            elements.sort()
            arr[(i-1)*k:(i+1)*k] = elements
        i+=1

    return arr

arr = sort_k_wiggled_better([1,2,5,4,7,11,9],2)
print arr