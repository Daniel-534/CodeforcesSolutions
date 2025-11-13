#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int t;
    cin >> t;
    
    while (t--) {
        long long n;
        cin >> n;
        long long ans = (n + 1) / 10;
        cout << ans << "\n";
    }
    return 0;
}
