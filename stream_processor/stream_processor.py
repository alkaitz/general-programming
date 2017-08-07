'''
Created on Aug 7, 2017

@author: alkaitz
'''

import heapq

'''
    You have a function that will be called with a stream of strings.
    Every time you receive a new word, you should return the length of the longest
    word that you have received that has showed in the string only once. Ex:
    f("Yes") -> 3
    f("No")  -> 3
    f("Yes") -> 2
'''

working_set = []
heapq.heapify(working_set)
repeated = set()

'''
    Structure will be sorted by negative numbers to transform it from a min heap to a max heap.
    Storing the tuple, to provide right sorting.
    None returned if data set is empty (all received words have appeared more than once)
'''
def process(str):
    if str not in repeated:
        if (-len(str),str) not in working_set:
            heapq.heappush(working_set, (-len(str),str))
        else:
            working_set.remove((-len(str),str))
            repeated.add(str)
    (length, _) = (working_set[0]) if working_set else (None, None)
    return -length if length else None

if __name__ == '__main__':
    assert(process("Hello") == 5)
    assert(process("Hello") == None)
    assert(process("Hallo") == 5)
    assert(process("Bye") == 5)
    assert(process("By") == 5)
    assert(process("B") == 5)
    assert(process("Hallo") == 3)
    assert(process("By") == 3)
    assert(process("Bye") == 1)
    print "Successful"