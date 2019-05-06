#include <stdio.h>

void bubble_sort(int a[], int n) {
   int i = 0, j = 0, ic = 0, jc=0, kc=0, tmp;
   for (i = 0; i < n; i++) {   // loop n times - 1 per element
      ic++;
       for (j = 0; j < n - i - 1; j++) { // last i elements are sorted already
        jc++;
            if (a[j] > a[j + 1]) {  // swop if order is broken
               tmp = a[j];
               a[j] = a[j + 1];
               a[j + 1] = tmp;
               kc++;
           }
       }
   }
   printf("ic:%d, jc:%d, kc:%d\n", ic,jc,kc);
}