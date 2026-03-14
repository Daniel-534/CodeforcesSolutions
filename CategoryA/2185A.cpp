#include <bits/stdc++.h>

using namespace std;

#define rep(i, n) for (int i = 1; i <= n; i++)

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int t;
    cin >> t;
    
    while (t--) {
        int n;
        cin >> n;
        
        rep(i,n) {
            cout << i;
            if (i < n) cout << " ";
        }
        cout << "\n";
    }
    
    return 0;
}
