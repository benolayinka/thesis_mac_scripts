void ddot_r(int dx[], int dy[], int n)
{
  int i, dtemp;
 for (i=0;i < n; i++)
     dtemp = dtemp + dx[i]*dy[i];
 return;
}