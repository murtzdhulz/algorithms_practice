__author__ = 'Murtaza'

# Get all combination of parenthesis for a given n. (n=number of parenthesis)
def parenthesis_recurse(result,left_rem,right_rem,str):
    # print left_rem,right_rem
    if left_rem < 0 or right_rem < left_rem:
        print 'Invalid state'
        return

    if left_rem==0 and right_rem==0:
        result.append(''.join(str))
        # print "All done here"
    else:
        #In recursion whatever is put in the current iteration is what you pop off immediately
        if left_rem>0:
            # print "putting ("
            str.append('(')
            parenthesis_recurse(result,left_rem-1,right_rem,str)
            str.pop()
        if right_rem>left_rem:
            # print "putting )"
            str.append(')')
            parenthesis_recurse(result,left_rem,right_rem-1,str)
            str.pop()
    return result

print parenthesis_recurse([],2,2,[])