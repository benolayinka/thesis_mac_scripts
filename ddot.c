#define RANDOM_DATA -486482214,-418856181,930282014,-347347496,-138348819,-988261325,815146594,-867907548,408358427,-669950624
#define RANDOM_DATA_SIZE 10;

void ddot_r()
{
	int n = RANDOM_DATA_SIZE;
	int dx[] = {RANDOM_DATA};
	int dy[] = {RANDOM_DATA};
	int dtemp = 0;
	int i;
	for(i=0;i < n; i++)
	{
		dtemp = dtemp + dx[i]*dy[i];
	}
 return;
}

void main()
{
	ddot_r();
}