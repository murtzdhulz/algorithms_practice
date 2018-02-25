
def count_eval(exp,result,map):
    if len(exp)==0:
        return 0
    if len(exp)==1:
        return 1 if bool_value(exp)==result else 0
    if str(result)+exp in map:
        return map[str(result)+exp]

    ways=0
    for i in xrange(1,len(exp),2):
        op=exp[i]
        left=exp[:i]
        right=exp[i+1:]
        left_true=count_eval(left,True,map)
        left_false=count_eval(left,False,map)
        right_true=count_eval(right,True,map)
        right_false=count_eval(right,False,map)
        total=(left_true+left_false)*(right_true+right_false)

        total_true=0
        if op=='^':
            total_true=left_true*right_false+left_false*right_true
        elif op=='&':
            total_true=left_true*right_true
        elif op=='|':
            total_true=left_true*right_false+left_false*right_true+left_true*right_true

        if result==True:
            ways+=total_true
        else:
            ways+=(total-total_true)

    map[str(result)+exp]=ways
    return ways

def bool_value(s):
    if s[0]=='1':
        return True
    return False

print count_eval("1^0|0|1",False,{})
print count_eval("0&0&0&1^1|0",True,{})