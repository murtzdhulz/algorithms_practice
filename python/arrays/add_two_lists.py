def add_lists(l1, l2):
    res_len=len(l1) if len(l1)>=len(l2) else len(l2)
    res=[]
    carry=0
    for i in xrange(res_len):
        cur_val=0
        if i<len(l1):
            cur_val+=l1[i]
        if i<len(l2):
            cur_val+=l2[i]
        cur_val+=carry
        res.append(cur_val%10)
        carry=cur_val/10

    if carry:
        res.append(carry)

    return res

print add_lists([1,2,3],[7,8,6])
print add_lists([9,9],[9,9])