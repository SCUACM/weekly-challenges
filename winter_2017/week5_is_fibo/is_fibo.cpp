#include <iostream>
#include <cmath>

using namespace std;

typedef long long value_type;

bool isFibo(const value_type & x) {
    long double sqrt_a = sqrt((5 * x * x) + 4);
    long double sqrt_b = sqrt((5 * x * x) - 4);
    long double comp_a;
    long double comp_b;

    if (modf(sqrt_a, &comp_a) == 0.0 || modf(sqrt_b, &comp_b) == 0.0) {
        return true;
    }
    return false;
}

int main() {
    value_type cases;
    cin >> cases;
    value_type values[cases];
    for (value_type i = 0; i < cases; i++) {
        cin >> values[i];
    }
    for (value_type i = 0; i < cases; i++) {
        if (isFibo(values[i])) {
            cout << "IsFibo" << endl;
        } else {
            cout << "IsNotFibo" << endl;
        }
    }

    return 0;
}
