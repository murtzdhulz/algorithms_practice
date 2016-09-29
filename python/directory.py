"""
Directory input will be like
dir1
    dir11
    dir12
        abc.png
    k.png
    dir13
        l.txt
th.jpg
"""
import os

def getPaths1(dir):
    dir_arr=[]
    cur_path=""
    paths=[]

    for line in dir.split('\n'):
        # print line,len(line)-len(line.strip())
        print line
        cur_line=line.strip()
        level=len(line)-len(cur_line)

        while(len(dir_arr)!=level):
            cur_ele=dir_arr.pop()
            # print 'Before',cur_path,cur_ele
            cur_path=cur_path[:-(len(cur_ele)+1)]
            # print 'After',cur_path

        dir_arr.append(line.strip())
        cur_path=os.path.join(cur_path,line.strip())

        # print dir_arr, cur_path

        if '.png' in line or '.jpg' in line:
            paths.append(cur_path)
            # OR paths.append('/'.join(dir_arr))

    return paths

def getPaths2(dir):
    dir_arr=[]
    paths=[]

    for line in dir.split('\n'):
        cur_line=line.strip()
        level=len(line)-len(cur_line)

        # Pop everything up until the level at which you want to push
        while(len(dir_arr)!=level):
            dir_arr.pop()

        dir_arr.append(line.strip())

        if '.png' in line or '.jpg' in line:
            paths.append('/'.join(dir_arr))

    return paths

dir_str="""\
dir1
 dir11
 dir12
  abc.png
 dir14
  dir15
   dir16
    Yo.png
 k.png
 dir13
  l.txt
th.jpg"""
print getPaths1(dir_str)
print getPaths2(dir_str)