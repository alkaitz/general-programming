'''
Created on Aug 10, 2017

@author: alkaitz
'''

'''
    What digit is the most common between 1 and 1,000 (inclusive)
'''

def count_digits(number):
    counters = [0] * 10
    for ch in str(number):
        counters[int(ch) - int('0')] += 1
    return counters

def sum_counters(accumulator, b):
    for i in range(len(accumulator)):
        accumulator[i] += b[i]

def count_digits_until(number):
    result = [0] * 10
    for i in range(1, number + 1):
        sum_counters(result, count_digits(i))
    return result

def max_digit_until(number):
    counters = count_digits_until(number)
    return counters.index(max(counters))

if __name__ == '__main__':
    def test_count_digits():
        assert(count_digits(1)      == [0,1,0,0,0,0,0,0,0,0])
        assert(count_digits(554321) == [0,1,1,1,1,2,0,0,0,0])
        assert(count_digits(1000)   == [3,1,0,0,0,0,0,0,0,0])

    def test_sum_counters():
        a = [1,2]
        sum_counters(a, [3,4])
        assert(a == [4,6])

    def test_digits_until():
        assert(count_digits_until(10) == [1, 2, 1, 1, 1, 1, 1, 1, 1, 1])
        assert(count_digits_until(100) == [11, 21, 20, 20, 20, 20, 20, 20, 20, 20])

    def test_max_digit_until():
        assert(max_digit_until(10) == 1)
        assert(max_digit_until(1000) == 1)

    test_count_digits()
    test_sum_counters()
    test_digits_until()
    test_max_digit_until()
    print max_digit_until(1000), "is the most common digit between 1 and 1,000 (inclusive)"
    print count_digits_until(1000)
    print "Successful"