import sys
sys.path.append( './lizard' )
import lizard

if __name__ == '__main__':
	lizard.main(['/Users/ben/thesis/lizard/lizard.py', './bubblesort.c', '-Einstructioncount'])