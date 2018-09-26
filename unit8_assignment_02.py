__author__ = 'Kalyan'

from placeholders import *


profiling_timeit = '''
Python also gives a helpful timeit module that can be used for benchmarking a given piece of code

Reading material:
 http://docs.python.org/3/library/timeit.html
 http://stackoverflow.com/questions/8220801/how-to-use-timeit-correctly
 http://www.dreamincode.net/forums/topic/288071-timeit-module/

Try out on sample code snippets from above links on your own before you get to the assignment.

Generally you will study performance as you vary the input across a range e.g. count = 10, 100, 1000, 10000

profile the 4 methods in unit7_conversion_methods.py using timeit in this assignment.

for each value of count, execute the method 5 times using timeit and print out the min value and the actual 5 values.
output should look like (a total of 16 lines):
numbers_string1, count = 10, min = 0.0001, actuals = [0.0001, 0.0002, 0.0001, ...]
numbers_string1, count = 100, min = 0.002, actuals = [0.002, 0.002, 0.003, ...]
....
numbers_string4, count = 10000, min = 0.1 actuals = [....]

'''

from unit8_conversion_methods import *
import timeit

def profile_timeit():
    list1 = ['numbers_string1', 'numbers_string2', 'numbers_string3', 'num_strings4']
    l = iter(list1)
    c = [10, 100, 1000, 10000]
    while True:
        try:
            k = next(l)
            for i in range(4):
                count1 = c[i]

                start = timeit.repeat(stmt='k1(' +str(count1)+ ')',setup='from unit8_conversion_methods import '+k+' as k1',repeat=5,number=1)

                t = ["%.6f" % k for k in start]
                min1 = min(t)
                p = "{0}, count = {1}, min = {2}, actuals = [{3}]".format(k, count1, min1, ", ".join(t))
                print(p)
        except StopIteration:
            break


# write your findings on what you learnt about timeit, measuring perf and how the results here compare to
# values in assignment1
summary = '''


'''

if __name__ == "__main__":
    profile_timeit()
