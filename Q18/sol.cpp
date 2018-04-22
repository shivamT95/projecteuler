#include <bits/stdc++.h>
using namespace std;

long long int DP[101][101];
long long int triangle[101][101];

int main()
{
	int N=15,i,j;
	for(i = 1; i <= N; ++i)
	{
		for(j = 1; j <= i; ++j)
			cin >> triangle[i][j];
	}

	DP[1][1] = triangle[1][1];
	for(i = 2; i <= N; ++i)
	{
		DP[i][1] = DP[i-1][1] + triangle[i][1];
		for(j = 2; j < N; ++j)
		{
			DP[i][j] = triangle[i][j] + max(DP[i-1][j], DP[i-1][j-1]);
		}
		DP[i][j] = DP[i-1][j-1]+triangle[i][j];
	}
	long long int ans = -1;
	for(j = 1; j <= N; ++j)
		ans = max(ans, DP[N][j]);

	cout << ans;
}