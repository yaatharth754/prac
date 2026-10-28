#include <iostream>
using namespace std;

long long recur(int n) {
    if (n <= 1)
        return n;
    return recur(n - 1) + recur(n - 2);
}

long long nonrecur(int n) {
    long long a = 0, b = 1, c;

    for (int i = 2; i <= n; i++) {
        c = a + b;
        a = b;
        b = c;
    }

    return (n == 0) ? a : b;
}

int main() {
    int n;
    cout <<"Enter a number: ";
    cin >> n;

    cout << "Recursive: " << recur(n) << endl;
    cout << "Non-recursive: " << nonrecur(n) << endl;

    return 0;
}
