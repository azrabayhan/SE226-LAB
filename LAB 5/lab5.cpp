#include <iostream>
using namespace std;


double Sn(int n) {
    if (n == 1) {
        return 1.0; 
    } else {
        
        double term = (n % 2 == 0 ? -1.0 : 1.0) / n;
        return term + Sn(n - 1);
    }
}

int main() {
    int n;
    cout << "Enter n: ";
    cin >> n;

    double result = Sn(n);
    cout << "S_" << n << " = " << result << endl;

    return 0;
}