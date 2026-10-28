
#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <algorithm>
using namespace std;

int partition(vector<int>& a, int low, int high) {
    int pivot = a[high], i = low - 1;

    for (int j = low; j < high; j++) {
        if (a[j] <= pivot)
            swap(a[++i], a[j]);
    }

    swap(a[i + 1], a[high]);
    return i + 1;
}

void quickSort(vector<int>& a, int low, int high, bool random) {
    if (low >= high)
        return;

    if (random) {
        int r = low + rand() % (high - low + 1);
        swap(a[r], a[high]);
    }

    int p = partition(a, low, high);
    quickSort(a, low, p - 1, random);
    quickSort(a, p + 1, high, random);
}

int main() {
    int n;
    cout <<"Enter the number of elements: ";
    cin >> n;

    vector<int> a(n);

    for (int i = 0; i < n; i++)
        cin >> a[i];

    vector<int> b = a;
    srand(time(0));

    quickSort(a, 0, n - 1, false);
    quickSort(b, 0, n - 1, true);

    cout << "Deterministic Quick Sort: ";
    for (int x : a) cout << x << " ";

    cout << "\nRandomized Quick Sort: ";
    for (int x : b) cout << x << " ";

    cout << endl;
    return 0;
}

//5
//8 3 6 1 4