__author__ = 'Murtaza'

if __name__ == "__main__":
    arr = [3, 7, 90, 20, 10, 50, 40]
    k = 3

    res_idx = 0
    cur_sum = sum(arr[:k])
    min_sum = cur_sum

    for i in range(k,len(arr)):
        cur_sum = cur_sum - arr[i-k] + arr[i]
        if cur_sum<min_sum:
            min_sum=cur_sum
            res_idx=i-k+1

    print res_idx,res_idx+k-1
    print arr[res_idx:res_idx+k]