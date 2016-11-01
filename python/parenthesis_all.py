__author__ = 'Murtaza'

# Get all combination of parenthesis for a given n. (n=number of parenthesis)
def parenthesis_recurse(result,left_rem,right_rem,str):
    # print left_rem,right_rem
    if left_rem < 0 or right_rem < left_rem:
        print 'Invalid state'
        return

    if left_rem==0 and right_rem==0:
        result.append(''.join(str))
    else:
        if left_rem>0:
            str.append('(')
            parenthesis_recurse(result,left_rem-1,right_rem,str)
            str.pop()
        if right_rem>left_rem:
            str.append(')')
            parenthesis_recurse(result,left_rem,right_rem-1,str)
            str.pop()
    return result

print parenthesis_recurse([],3,3,[])