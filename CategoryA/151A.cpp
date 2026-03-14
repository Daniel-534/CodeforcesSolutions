#include <bits/stdc++.h>
 
using namespace std;
 
typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pi;

#define rep(i, n) for (int i = 1; i <= n; i++)
 
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
	int n, k, l, c, d, p, nl, np;
	cin >> n >> k >> l >> c >> d >> p >> nl >> np;

	int aux1 = k*l/nl;
	int aux2 = c*d;
	int aux3= p/np;

	vi aux = {aux1,aux2,aux3};

	cout << *min_element(aux.begin(),aux.end()) / n << endl;

	return 0;
}
