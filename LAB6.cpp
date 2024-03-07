#include <iostream>

using namespace std;

double function(double n) {
    if (n == 0)
        return 1;
    else
        return (n / (n + 2) - 10) * function(n - 1);
}

double function() {
    int number2;
    cout << "Enter the number: " << endl;
    cin >> number2;
    double product = 1;
    while (number2 != 0) {
        product = product * (((double) number2 / (double) (number2 + 2)) - 10);
        number2--;
    }
    cout << "Your result is: " << product << endl;
}

int main() {
    int number;
    cout << "Enter the number: " << endl;
    cin >> number;
    cout << "Your result is: " << function(number) << endl;
    function();
    return 0;
}