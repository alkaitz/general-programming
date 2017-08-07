'''
Created on Aug 7, 2017

@author: alkaitz
'''

'''
    You have two arrays (a and i). a contains a list of integers and i contains the index
    in order to relocate the contents of a. For instance:
    a = [5,10,15]
    i = [2,0,1]
    output = [10,15,5]
'''

def index_array(a, i):
    for index in range(len(i)):
        while i[index] != index:
            indexOrigin = index
            indexTarget = i[index]
            a[indexOrigin], a[indexTarget] = a[indexTarget], a[indexOrigin]
            i[indexOrigin], i[indexTarget] = i[indexTarget], i[indexOrigin]

if __name__ == '__main__':
    a = [5,10,15]
    i = [2,0,1]
    index_array(a,i)
    assert(a == [10,15,5])
    a = [1,2,3,4,5,6,7,8]
    i = [7,6,5,4,3,2,1,0]
    index_array(a,i)
    assert(a == [8,7,6,5,4,3,2,1])
    print "Successful"