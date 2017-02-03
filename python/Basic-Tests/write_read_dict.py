__author__ = 'Murtaza'
import pickle

def write_dict(d):
    with open("some_dict","wb") as file:
        pickle.dump(d,file)

def read_dict(file_name):
    with open("some_dict","rb") as file:
        d=pickle.load(file)
    print type(d)
    print d

dictionary={("Label1","Word1"):3,("Label2","Word1"):5}
# dictionary={1:"Apple",2:"Orange"}
# print dictionary,type(dictionary)
# write_dict(dictionary)
# read_dict("some_dict")
