#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int t;
    cin >> t;
    
    while (t--) {
        int n;
        cin >> n;
        
        // Inicializar con valores por defecto para evitar warnings
        int minimo = INT_MAX;
        int maximo = INT_MIN;
        
        for (int i = 0; i < n; i++) {
            int x;
            cin >> x;
            if (x < minimo) minimo = x;
            if (x > maximo) maximo = x;
        }
        cout << maximo - minimo << "\n";
    }
    return 0;
}
