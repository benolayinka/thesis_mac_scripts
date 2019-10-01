import sys
sys.path.append( './lizard' )
import lizard

#add test filenames to this list
tests = ['./bubblesort.c', './ddot.c']

if __name__ == '__main__':
	for test in tests:
		lizard.main(['/Users/ben/thesis/lizard/lizard.py', test, '-Einstructioncount'])