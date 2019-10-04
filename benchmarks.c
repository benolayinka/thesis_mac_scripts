

/*****************************************************************************
 * benchmarks.c
 *****************************************************************************/

#include <sys/platform.h>
#include "adi_initialize.h"
#include "benchmarks.h"

#include <string.h>
#include <cycle_count.h>
#include <stdio.h>

#include "test.h"

#define STRINGIZE_(TEST) #TEST
#define STRINGIZE(TEST) STRINGIZE_(TEST)

#define TEST_NAME_LENGTH 50

#define RANDOM_DATA_SIZE 10
#define RANDOM_DATA -486482214,-418856181,930282014,-347347496,-138348819,-988261325,815146594,-867907548,408358427,-669950624

#if SIM
#define NUMBENCHMARKS 1
#else
#define NUMBENCHMARKS 50000
#endif

void benchmark(void func());
void ddot_r();
void bubble_sort();
void no_test();

/** 
 * If you want to use command program arguments, then place them in the following string. 
 */
char __argv_string[] = "";

void no_test()
{
    return;
}

void bubble_sort() {
	int a[] = {RANDOM_DATA};
	int n = RANDOM_DATA_SIZE;
   int i = 0, j = 0, tmp;
   for (i = 0; i < n; i++) {   // loop n times - 1 per element
       for (j = 0; j < n - i - 1; j++) { // last i elements are sorted already
            if (a[j] > a[j + 1]) {  // swop if order is broken
               tmp = a[j];
               a[j] = a[j + 1];
               a[j + 1] = tmp;
           }
       }
   }
}

void ddot_r()
       {
		int n = RANDOM_DATA_SIZE;
		int dx[] = {RANDOM_DATA};
		int dy[] = {RANDOM_DATA};
       int dtemp;
       int i;

       dtemp = 0;

       for (i=0;i < n; i++)
           dtemp = dtemp + dx[i]*dy[i];
       return;
}

void pwm()
{
	int pwmval = 127;
	bool pwm_on = 0;
	for(int soft = 0; soft < 0xff; soft++)
	{
		if(soft == 0)
			pwm_on = true;

		else if(soft == pwmval)
			pwm_on = false;
	}
}

#define FR32_MAX 2^32
void bilinear()
    {
		volatile int xx = -486482214;
		volatile int xy = -418856181;
		volatile int yx = 930282014;
		volatile int yy = -347347496;
		volatile int x = -138348819;
		volatile int y = -988261325;

        const int xInv = FR32_MAX - x;
        const int yInv = FR32_MAX - y;

        int bilinear = xx * xInv * yInv +
        xy * x * yInv +
        yx * xInv * y +
        yy * x * y;
    }

int main(int argc, char *argv[])
{
	#if TEST == 0
		#define TESTNAME "notest"
		benchmark(no_test);
	#elif TEST == 1
		#define TESTNAME "bubblesort1"
        benchmark(bubble_sort);
	#elif TEST == 2
		#define TESTNAME "ddot1"
        benchmark(ddot_r);
	#elif TEST == 3
	#define TESTNAME "pwm1"
    benchmark(pwm);
	#elif TEST == 4
	#define TESTNAME "bilinear1"
    benchmark(bilinear);
	#elif TEST >= 5
		#define TESTNAME "end"
		benchmark(no_test, 0, 0);
	#else
		#define TESTNAME "undefined"
		benchmark(no_test, 0, 0);
	#endif

	return 0;
}

//https://gist.github.com/RenatoUtsch/4162799
void benchmark(void (*func)())
{
	cycle_t start_count;
	cycle_t final_count;
	cycle_t total_count = 0;
	int i;

	for(i = 0; i < NUMBENCHMARKS; ++i)
		{
		START_CYCLE_COUNT(start_count);

		/* Call the function to benchmark. */
		func();

		STOP_CYCLE_COUNT(final_count,start_count);
		total_count += final_count;
		}
	char test_name[TEST_NAME_LENGTH + 1]; //MAX LENGTH!!!
	strcpy(test_name, TESTNAME);
	printf("%s\n", test_name);
	PRINT_CYCLES("cycles:", total_count);
	printf("test#: %s\n", STRINGIZE(TEST));
	printf("numbenchmarks: %d\n", NUMBENCHMARKS);
	printf("cycles per benchmark: %d\n", total_count/NUMBENCHMARKS);
}
