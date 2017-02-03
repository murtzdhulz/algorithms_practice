__author__ = 'Murtaza'

def longest_word(string_arr):
    # create a map for lookup
    map={}
    for s in string_arr:
        map[s]=True

    string_arr.sort(key=lambda s:len(s),reverse=True)
    for s in string_arr:
        # print "Processing String:",s
        if canbuildword(s,True,map):
            return s

    return ""

def canbuildword(string,originalword,map):
    if map.has_key(string) and not originalword:
        return map.get(string)

    for i in range(1,len(string)):
        left=string[:i]
        right=string[i:]
        if map.has_key(left) and map.get(left)==True and canbuildword(right,False,map):
            return True

    # print "Adding to cache with False:",string
    map[string]=False
    return False

print longest_word(["hello","thisisalongstring","this","long","a","string","thisisstring","is","thisisalongstringyesyes"])