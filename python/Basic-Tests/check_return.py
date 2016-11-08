def check_return():
    return True,"Hello", 5

print type(check_return())
li=list(check_return())
print li
print type(li)
print check_return()[2]