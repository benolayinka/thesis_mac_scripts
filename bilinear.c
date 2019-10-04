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

void main()
{
    bilinear();
}