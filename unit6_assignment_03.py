__author__ = 'Kalyan'

notes = '''
 This problem will require you to put together many things you have learnt
 in earlier units to solve a problem.

 In particular you will use functions, nested functions, file i/o, functions, lists, dicts, iterators, generators,
 comprehensions,  sorting etc.

 Read the constraints carefully and account for all of them. This is slightly
 bigger than problems you have seen so far, so decompose it to smaller problems
 and solve and test them independently and finally put them together.

 Write subroutines which solve specific subproblems and test them independently instead of writing one big
 mammoth function.

 Do not modify the input file, the same constraints for processing input hold as for unit6_assignment_02
'''

problem = '''
 Given an input file of words (mixed case). Group those words into anagram groups and write them
 into the destination file so that words in larger anagram groups come before words in smaller anagram sets.

 With in an anagram group, order them in case insensitive ascending sorting order.

 If 2 anagram groups have same count, then set with smaller starting word comes first.

 For e.g. if source contains (ant, Tan, cat, TAC, Act, bat, Tab), the anagram groups are (ant, Tan), (bat, Tab)
 and (Act, cat, TAC) and destination should contain Act, cat, TAC, ant, Tan, bat, Tab (one word in each line).
 the (ant, Tan) set comes before (bat, Tab) as ant < bat.

 At first sight, this looks like a big problem, but you can decompose into smaller problems and crack each one.

 source - file containing words, one word per line, some words may be capitalized, some may not be.
 - read words from the source file.
 - group them into anagrams. how?
 - sort each group in a case insensitive manner
 - sort these groups by length (desc) and in case of tie, the first word of each group
 - write out these groups into destination
'''

import unit6utils
import string
import os
import inspect
from collections import Counter
import itertools

def open_input_file(file, mode="rt"):
    mod_dir = get_module_dir()
    test_file = os.path.join(mod_dir, file)
    return open(test_file, mode)

def get_module_dir():
    mod_file = inspect.getfile(inspect.currentframe())
    mod_dir = os.path.dirname(mod_file)
    return mod_dir

def open_temp_file(file, mode):
    data_dir = os.getenv("DATA_DIR", default=get_temp_dir())
    out_file = os.path.join(data_dir, file)
    return open(out_file, mode)

def get_temp_dir():
    module_dir = get_module_dir()
    temp_dir = os.path.join(module_dir, "tempfiles")
    if not os.path.exists(temp_dir):
        os.mkdir(temp_dir)
    return temp_dir


def anagram_sort(source, destination):
    f = open_input_file(source)
    lines = []
    # this will not read the whole file into memory like readlines would.
    for x in f:
        lines.append(x)
    lines.remove('\n')
    for i in lines:
        if i[0] == '#' or i[0] == " ":
            lines.remove(i)
    x = "".join(lines).split('\n')
    y="".join(lines).split('\n')
    x = ",".join(x)
    y = ",".join(y).lower()
    y = y.split(',')
    x = x.split(',')

    from itertools import groupby
    out = [list(group) for key, group in itertools.groupby(sorted(y, key=sorted), sorted)]
    out.sort()
    out.sort(key=len)
    out.sort(key=len,reverse=True)
    for i in out:
        i.sort()
    for i in out:
        for j in i:
            if j in x:
                x.remove(j)
                continue
            else:
                for k in x:
                    if (k.lower()) == (j):
                        n = i.index(j)
                        i.remove(j)
                        i.insert(n, k)
                        x.remove(k)
                        break
    f = open_temp_file(destination, "w")  # same as "wt"
    for i in out:
        for j in i:
          f.write(j)
          f.write('\n')
    f.close()



def test_anagram_sort():
    source = unit6utils.get_input_file("unit6_testinput_03.txt")
    expected = unit6utils.get_input_file("unit6_expectedoutput_03.txt")
    destination = unit6utils.get_temp_file("unit6_output_03.txt")
    anagram_sort(source, destination)
    result = [word.strip() for word in open(destination)]
    expected = [word.strip() for word in open(expected)]
    assert expected == result
