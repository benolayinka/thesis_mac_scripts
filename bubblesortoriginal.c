void bubble_sort(int a[], int n) {
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