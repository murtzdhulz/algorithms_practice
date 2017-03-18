__author__ = 'Murtaza'

def longest_palindromic_substring(s):
    max_len,start,end=1,0,0

    for i in range(1,len(s)):
        # find even length palindrome starting between i-1 and i
        len1=expand_from_center(i-1,i,s)
        len2=expand_from_center(i-1,i+1,s)
        length=max(len1,len2)
        if length>max_len:
            max_len=length
            start=i-length/2
            end=i+(length-1)/2
    return s[start:end+1],max_len

def expand_from_center(left,right,s):
    while left>=0 and right<len(s) and s[left]==s[right]:
        left-=1
        right+=1
    return right-left-1

print longest_palindromic_substring("abahiyoooooooy")
