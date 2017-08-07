'''
Created on Aug 1, 2017

@author: alkaitz
'''

'''
    An integer array defines the height of a 2D set of columns. After it rains enough amount of water,
    how much water will be contained in the valleys formed by these mountains?
    Ex: [3 2 3]
    X   X    X W X
    X X X -> X X X -> 1
    X X X    X X X
'''

def water_level(a):
    if not a:
        raise "Array cannot be empty"
    water = 0
    leftIndex, rightIndex = 0, len(a) - 1
    left, right = a[0], a[-1]
    while leftIndex <= rightIndex:
        if left <= right:
            water += max(left - a[leftIndex], 0)
            left = max(left, a[leftIndex])
            leftIndex += 1
        else:
            water += max(right - a[rightIndex], 0)
            right = max(right, a[rightIndex])
            rightIndex -= 1
    return water

if __name__ == '__main__':
    assert(water_level([3, 2, 3]) == 1)
    assert(water_level([1, 2, 3, 4]) == 0)
    assert(water_level([5, 1, 3, 4]) == 4)
    assert(water_level([2, 1, 4, 3, 6]) == 2)
    print "Successful"