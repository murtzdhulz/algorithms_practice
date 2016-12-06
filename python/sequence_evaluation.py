# 2-3-5*7/2+1

def compute_sequence(s):
    number_stack = []
    op_stack = []

    i=0
    while i<len(s):
        # print "I value:",i
        num = parse_number(s,i)
        # print "Pushing to num stack",num
        number_stack.append(float(num))

        i+=len(str(num))
        if i>=len(s):
            break

        op = s[i]
        collapse_top(number_stack,op_stack,op)
        op_stack.append(op)
        i+=1

    collapse_top(number_stack,op_stack,'end')

    if len(number_stack) == 1 and len(op_stack) == 0:
        return number_stack.pop()
    return 0

def collapse_top(n,o,op):
    priority={'+':1,'-':1,'*':2,'/':2,'end':0}
    while len(n)>=2 and len(o)>=1:
        if priority[op] <= priority[o[-1]]:
            cur_op = o.pop()
            num2=n.pop()
            num1=n.pop()
            n.append(apply_op(num1,num2,cur_op))
        else:
            break

def apply_op(n1,n2,op):
    if op=='+':
        return n1+n2
    if op=='-':
        return n1-n2
    if op=='*':
        return n1*n2
    if op=='/':
        return n1/n2

def parse_number(s,offset):
    num = []
    while offset<len(s) and s[offset].isdigit():
        num.append(s[offset])
        offset+=1
    return int(''.join(num))

print compute_sequence('2-6-7*8/2+5')
