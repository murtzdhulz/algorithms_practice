def get_words(letters,dic):
    arr_letters=[0]*26
    for l in letters:
        idx=ord(l)-ord('a')
        # print idx
        arr_letters[idx]+=1

    res = []
    for word in dic:
        flag=True
        arr_check=[0]*26
        for l in word:
            idx=ord(l)-ord('a')
            arr_check[idx]+=1
            if arr_check[idx]>arr_letters[idx]:
                flag=False
                break
        if flag:
            res.append(word)
    return res

def get_words_strict(letters,dic):
    arr_letters=[0]*26
    for l in letters:
        idx=ord(l)-ord('a')
        # print idx
        arr_letters[idx]+=1

    res = []
    for word in dic:
        if len(word)!=len(letters):
            continue
        flag=True
        arr_check=[0]*26
        for l in word:
            idx=ord(l)-ord('a')
            arr_check[idx]+=1
            if arr_check[idx]>arr_letters[idx]:
                flag=False
                break
        if flag:
            res.append(word)
    return res

print get_words(['a','b','d','a','p'],['badaa','pad','azza'])

print get_words_strict(['a','b','d','a','p'],['badap','pad','azza'])