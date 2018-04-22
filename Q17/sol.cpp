#include <bits/stdc++.h>
using namespace std;

int dig1[20] = {4,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8};
int dig2[10] = {0,3,6,6,5,5,5,7,6,6};

int main()
{
	int ans = 0;

	for(int i = 1; i <= 1000; ++i)
	{
		int cur = i, flag = 0;
		if(cur >= 1000)
		{
			ans += dig1[cur/1000]+8;
			cur = cur % 1000;
			flag = 1;
		}
		if(cur >= 100)
		{
			ans += dig1[cur/100]+7;
			cur = cur%100;
			flag = 1;
		}
		if(cur)
		{
			if(flag)
				ans += 3;

			if(cur < 20)
				ans += dig1[cur];
			else
			{
				ans += dig2[cur/10];
				cur = cur%10;
				if(cur)
					ans += dig1[cur];
			}
		}
	}
	cout << ans;
}