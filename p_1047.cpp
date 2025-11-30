#include <iostream>
using namespace std;

int main() {
    int hi, mi, hf, mf;
    cin >> hi >> mi >> hf >> mf;
    int start = hi * 60 + mi;
    int end = hf * 60 + mf;
    if (end <= start) {
        end += 24 * 60;
    }
    int duration = end - start;
    int hours = duration / 60;
    int minutes = duration % 60;
    cout << "O JOGO DUROU " << hours << " HORA(S) E " << minutes << " MINUTO(S)" << endl;
    return 0;
}

