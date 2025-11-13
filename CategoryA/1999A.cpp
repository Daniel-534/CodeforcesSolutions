
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int t;
    cin >> t;
    
    for (int i = 0; i < t; i++) {
        string n;
        cin >> n;
        
        int suma = 0;
        for (char caracter : n) {
            suma += caracter - '0';
        }
        cout << suma << "\n";
    }
    
    return 0;
}
