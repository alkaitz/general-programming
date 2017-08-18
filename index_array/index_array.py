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

def index_array(array, indexes):
    for index in range(len(indexes)):
        while indexes[index] != index:
            swapPositionsInArrays(array, indexes, index, i[index])

def swapPositionsInArrays(array, indexes, index1, index2):
    swapPositions(array, index1, index2)
    swapPositions(indexes, index1, index2)

def swapPositions(array, index1, index2):
    array[index1], array[index2] = array[index2], array[index1]

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