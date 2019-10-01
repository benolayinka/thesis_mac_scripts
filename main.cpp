#include "bubblesort.c"
#include "ddot.c"

#define RANDOM_DATA -486482214,-418856181,930282014,-347347496,-138348819,-988261325,815146594,-867907548,408358427,-669950624
#define RANDOM_DATA_SIZE 10;

int a[] = {RANDOM_DATA};
int dx[] = {RANDOM_DATA};
int dy[] = {RANDOM_DATA};
int n = RANDOM_DATA_SIZE;

void bubble_sort(int a[], int n);
void ddot_r(int dx[], int dy[], int n);

int main(){
	//bubble_sort(a, n);
	ddot_r(dx, dy, n);
	return 0;
}