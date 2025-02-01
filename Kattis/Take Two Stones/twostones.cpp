#include <iostream>
using namespace std;


void find_winner(int number_of_stones){
    if (number_of_stones % 2 == 1){
        cout << "Alice" << endl;
    }else {
        cout << "Bob" << endl;
    }
}

int main() {
    int number_of_stones {0};
    cin >> number_of_stones;
    find_winner(number_of_stones);
    return 0;
}