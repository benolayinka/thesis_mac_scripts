void pwm()
{
	int pwmval = 127;
	int pwm_on = 0;
	for(int soft = 0; soft < 0xff; soft++)
	{
		if(soft == 0)
			pwm_on = 0;

		else if(soft == pwmval)
			pwm_on = 1;
	}
}

void main()
{
	pwm();
}