#include <iostream>
#include <iomanip>
using namespace std;
int main() {
    double salary, tax = 0.0;
    cin >> salary;

    if (salary <= 2000.0) {
        cout << "Isento" << endl;
    }
    else {
        if (salary > 4500.0) {
            tax += (salary - 4500.0) * 0.28;
            salary = 4500.0;
        }
        if (salary > 3000.0) {
            tax += (salary - 3000.0) * 0.18;
            salary = 3000.0;
        }
        if (salary > 2000.0) {
            tax += (salary - 2000.0) * 0.08;
        }
        cout << fixed << setprecision(2)
        cout << "R$ " << tax << endl;
    }
    return 0;
}


