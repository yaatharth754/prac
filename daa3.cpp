
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct Item {
    int weight, profit;
    double ratio;
};

bool compare(Item a, Item b) {
    return a.ratio > b.ratio;
}

int main() {
    int n, capacity;
    cout <<"Enter the number of items: ";
    cin >> n;

    vector<Item> items(n);

    for (int i = 0; i < n; i++) {
        cin >> items[i].weight >> items[i].profit;
        items[i].ratio = (double)items[i].profit / items[i].weight;
    }
    cout <<"Enter the capacity of the knapsack: ";
    cin >> capacity;

    sort(items.begin(), items.end(), compare);

    double totalProfit = 0;

    for (int i = 0; i < n; i++) {
        if (items[i].weight <= capacity) {
            totalProfit += items[i].profit;
            capacity -= items[i].weight;
        } else {
            totalProfit += items[i].ratio * capacity;
            break;
        }
    }

    cout << "Maximum Profit: " << totalProfit << endl;

    return 0;
}

/*
3
10 60
20 100
30 120
50
*/