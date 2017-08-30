'''
Created on Aug 30, 2017

@author: alkaitz
'''

'''
    From a sorted list of integer numbers and a sum, find a pair of numbers
    which sum adds the argument provided
    e.g: [1, 2, 3, 9] 8 => None
         [1, 2, 4, 4] 8 => (4,4)
'''

def find_pair(a, sum):
    low, high = 0, len(a) - 1
    while low < high:
        result = a[low] + a[high]
        if  result == sum:
            return (a[low], a[high])
        if result < sum:
            low += 1
        else:
            high -= 1
    return None

if __name__ == '__main__':
    assert (find_pair([1, 2, 3, 9], 8) == None)
    assert (find_pair([1, 2, 4, 4], 8) == (4,4))
    assert (find_pair([1, 2, 4, 4], 6) == (2,4))
    print "Successful"