#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int n, respuesta;
    cin >> n;
    
    if (n % 5 == 0) {
        respuesta = n / 5;
    } else {
        respuesta = n / 5 + 1;
    }
    
    cout << respuesta << "\n";
    return 0;
}
