__author__ = 'Murtaza'

def is_permutation(s1,s2):
    if len(s1) != len(s2):
        return False

    char_counts = [0]*128
    for char in s1:
        char_counts[ord(char)] += 1

    for char in s2:
        char_counts[ord(char)] -= 1
        if char_counts[ord(char)]<0:
            return False

    return True

print is_permutation("bad","adb")
