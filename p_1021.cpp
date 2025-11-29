#include <iostream>
#include <cmath>
using namespace std;

int main() {
    double n;
    cin >> n;

    int notes, coins;
    int total = round(n * 100);

    cout << "NOTAS:\n";

    int note_values[] = {10000, 5000, 2000, 1000, 500, 200};

    for (int v : note_values) {
        notes = total / v;
        cout << notes << " nota(s) de R$ " << fixed;

        printf("%d.%02d\n", v/100, v%100);

        total = total % v;
    }

    // COINS
    cout << "MOEDAS:\n";

    int coin_values[] = {100, 50, 25, 10, 5, 1};

    for (int v : coin_values) {
        coins = total / v;
        cout << coins << " moeda(s) de R$ ";

        printf("%d.%02d\n", v/100, v%100);

        total = total % v;
    }

    return 0;
}

