#include <bits/stdc++.h>
using namespace std;

int mdays[12] = {31,28,31,30,31,30,31,31,30,31,30,31};
int main()
{
	int day,dayn,month,year,ans=0;
	for(day = 0, dayn = 1, month = 0, year = 1900; year < 2001; )
	{
		if(day == 6 && dayn == 1 && year > 1900)
			++ans;

		//cout << day << " " << dayn << "//" << month << "//" << year << endl;

		if(month == 1)
		{
			int tmp = 28;
			if((year % 100 == 0 && year % 400 == 0) || (year % 100 != 0 && year % 4 == 0))
				tmp = 29;
			
			if(dayn == tmp)
			{
				dayn = 1;
				month = (month+1) % 12;
			}
			else
				dayn++;
		}
		else
		{
			if(dayn == mdays[month])
			{
				dayn = 1;
				if(month == 11)
					year++;
				month = (month+1) % 12;
			}
			else
				dayn++;
		}
		day = (day + 1) % 7;
	}

	cout << ans;
}	