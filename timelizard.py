import sys
sys.path.append( './lizard' )
import lizard
import getinstr
import time
import os
from subprocess import call

#add test filenames to this list
tests = ['./bubblesort.c']

lizard_loops = 1
clang_loops = 1
lldb_loops = 1
total_time=[]

def mean(data):
    """Return the sample arithmetic mean of data."""
    n = len(data)
    if n < 1:
        raise ValueError('mean requires at least one data point')
    return sum(data)/n # in Python 2 use sum(data)/float(n)

def _ss(data):
    """Return sum of square deviations of sequence data."""
    c = mean(data)
    ss = sum((x-c)**2 for x in data)
    return ss

def stddev(data, ddof=0):
    """Calculates the population standard deviation
    by default; specify ddof=1 to compute the sample
    standard deviation."""
    n = len(data)
    if n < 2:
        raise ValueError('variance requires at least two data points')
    ss = _ss(data)
    pvar = ss/(n-ddof)
    return pvar**0.5

def stddev(data, ddof=0):
	return 0

if __name__ == '__main__':
	for test in tests:
		for _ in xrange(lizard_loops):
			start_time = time.time()
			lizard.main(['/Users/ben/thesis/lizard/lizard.py', test, '-Einstructioncount'])
			total_time.append(time.time()-start_time)

		mean_time = mean(total_time)
		std = stddev(total_time)
		print("Lizard & %s & %d & %d" % (mean_time, lizard_loops, std))
		total_time = []

		for _ in xrange(clang_loops):
			start_time = time.time()
			process = call(['clang', 'main.cpp'])
			total_time.append(time.time()-start_time)

		mean_time = mean(total_time)
		std = stddev(total_time)
		print("Clang & %s & %d & %d" % (mean_time, lizard_loops, std))
		total_time = []

		time.sleep(1)

		for _ in xrange(lldb_loops):
			start_time = time.time()
			getinstr.main('a.out')
			total_time.append(time.time()-start_time)

		mean_time = mean(total_time)
		std = stddev(total_time)
		print("LLDB & %s & %d & %d" % (mean_time, lizard_loops, std))