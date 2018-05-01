def add_binary_strings_v1(s1,s2):
    s1=s1[::-1]; s2=s2[::-1]
    res=""
    carry=0
    i=0; j=0
    while i<len(s1) and j<len(s2):
        cur_sum=int(s1[i])+int(s2[j])+carry
        res+=str(cur_sum%2)
        carry=cur_sum/2
        i+=1; j+=1
    while i<len(s1):
        cur_sum=int(s1[i])+carry
        res+=str(cur_sum%2)
        carry=cur_sum/2
        i+=1
    while j<len(s2):
        cur_sum=int(s2[i])+carry
        res+=str(cur_sum%2)
        carry=cur_sum/2
        j+=1
    if carry:
        res+=str(carry)
    return res[::-1]

def add_binary_strings_v2(s1,s2):
    res=""
    carry=0
    i=0
    j=0
    while len(s1)-i-1>=0 and len(s2)-j-1>=0:
        cur_sum=int(s1[len(s1)-i-1])+int(s2[len(s2)-j-1])+carry
        res=str(cur_sum%2)+res
        carry=cur_sum/2
        i+=1
        j+=1
    while len(s1)-i-1>=0:
        cur_sum=int(s1[len(s1)-i-1])+carry
        res=str(cur_sum%2)+res
        carry=cur_sum/2
        i+=1
    while len(s2)-j-1>=0:
        cur_sum=int(s2[len(s2)-j-1])+carry
        res=str(cur_sum%2)+res
        carry=cur_sum/2
        j+=1
    if carry:
        res=str(carry)+res
    return res

# print add_binary_strings_v2("10","110")