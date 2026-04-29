#include <bits/stdc++.h>
using namespace std;

struct Item {
    string name;
    double cost, value;
};


bool cmp(Item a, Item b) {
    return (a.value / a.cost) > (b.value / b.cost);
}


void fractionalKnapsack(vector<Item> items, double budget) {
    sort(items.begin(), items.end(), cmp);

    double totalValue = 0.0;

    cout << "\nSelected Items:\n";

    for (auto &item : items) {
        if (budget == 0) break;

        if (item.cost <= budget) {
       
            cout << "✔ " << item.name << " (Full)\n";
            budget -= item.cost;
            totalValue += item.value;
        } else {
          
            double fraction = budget / item.cost;
            cout << "✔ " << item.name << " (" << fraction * 100 << "%)\n";
            totalValue += item.value * fraction;
            budget = 0;
        }
    }

    cout << "\nTotal Value Obtained: " << totalValue << endl;
}


bool validNumber(double x) {
    return x > 0;
}

int main() {
    int choice;

    do {
        cout << "\n===== Budget Optimizer =====\n";
        cout << "1. Enter Items & Optimize\n";
        cout << "2. Exit\n";
        cout << "Enter choice: ";
        cin >> choice;

        if (choice == 1) {
            int n;
            double budget;

            cout << "\nEnter number of items: ";
            cin >> n;

            vector<Item> items(n);

            for (int i = 0; i < n; i++) {
                cout << "\nItem " << i + 1 << " Name: ";
                cin >> items[i].name;

                cout << "Cost: ";
                cin >> items[i].cost;

                cout << "Value: ";
                cin >> items[i].value;

                if (!validNumber(items[i].cost) || !validNumber(items[i].value)) {
                    cout << " Invalid input! Values must be positive.\n";
                    i--;
                }
            }

            cout << "\nEnter Budget: ";
            cin >> budget;

            if (!validNumber(budget)) {
                cout << " Invalid budget!\n";
                continue;
            }

            fractionalKnapsack(items, budget);
        }

    } while (choice != 2);

    cout << "\nExiting...\n";
    return 0;
}
