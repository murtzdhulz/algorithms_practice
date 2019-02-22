def get_from_file(filename):
    flag=False
    with open(filename,'rb') as f:
        for l in f:
            if flag:
                print l.strip()
                break
            if "Discharge Disposition:" in l.strip():
                flag=True

def get_disposition_from_string(text):
    flag=False
    for l in text.split("\n"):
        if flag:
            return l.strip()
        if "Discharge Disposition:" in l.strip():
            flag = True

with open("sample_note.txt",'rb') as f:
    data = f.readlines()
    data="".join(data)
    # print data

# print data
# get_disposition_from_string(data)