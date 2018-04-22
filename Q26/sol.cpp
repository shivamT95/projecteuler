#include <bits/stdc++.h>
using namespace std;

int used[1010];

int cntdigs(int n)
{
	int ans = 0;
	while(n)
	{
		ans++;
		n /= 10;
	}
	return ans;
}

int func(int den)	
{
	for(int i = 0; i < 1010; ++i)
		used[i] = -1;

	int num = 1, tans = 0;
	while(num)
	{
		if(num < den)
		{
			num *= 10;
		}
		else
		{
			int rem = num % den;
			int quo = num/den;
			tans += cntdigs(quo);
			num = (num - quo*den);

			if(used[rem] != -1)
				return tans-used[rem];

			used[rem] = tans;
		}
	}
	return 0;
}

int main()
{
	int ans = -1, d = -1, i;
	for(i = 1; i < 1000; ++i)
	{
		int tmp = func(i);
		if(tmp > ans)
		{
			ans = tmp;
			d = i;
		}
	}

	cout << d;
}