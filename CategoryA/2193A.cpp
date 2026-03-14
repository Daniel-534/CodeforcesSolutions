#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector<int> vi;

#define rep(i, n) for (int i = 0; i < n; i++)

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int t;
    cin >> t;
    while(t--) {
        int n, s, x;
        cin >> n >> s >> x;
        
        vi a(n);
        ll sum = 0;
        
        rep(i, n) {
            cin >> a[i];
            sum += a[i];
        }
        if(sum <= s) {
            if((s - sum) % x == 0) {
                cout << "YES\n";
            } else {
                cout << "NO\n";
            }
        } else {
            cout << "NO\n";
        }
    }
    
    return 0;
}
