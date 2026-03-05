#include <iostream>
using namespace std;


int main() {

//task1

    int n;

    cout << "Please enter a positive integer greater than 1: ";
    cin >> n;

    if (n <= 1) {
        cout << "You entered an invalid value." << endl;
        return 0;
    }

    int steps = 0;
    int current = n;

    
    while (current != 1) {
        cout << current << " → ";
        if (current % 2 == 0) {
            current /= 2;  
        } else {
            current = current * 3 + 1;  
        }
        steps++;
    }

    cout << "1" << endl;  
    cout << "Total steps: " << steps << endl;

    




//task2

    int x;
   
    do {
        cout << "Please enter a number between 10 and 100: ";
        cin >> x;
        if(x < 10 || x > 100)
            cout << "Invalid input. ";
    } while(x < 10 || x > 100);

    int fizzCount = 0, buzzCount = 0, fizzBuzzCount = 0;

    for(int i = 1; i <= x; i++) {
        
        if(i % 7 == 0) {
            cout << "(" << i << " is skipped)" << endl;
            continue;
        }

        if(i % 3 == 0 && i % 5 == 0) {
            cout << "FizzBuzz" << endl;
            fizzBuzzCount++;
        } else if(i % 3 == 0) {
            cout << "Fizz" << endl;
            fizzCount++;
        } else if(i % 5 == 0) {
            cout << "Buzz" << endl;
            buzzCount++;
        } else {
            cout << i << endl;
        }
    }

    
    cout << "--- Summary ---" << endl;
    cout << "Fizz count : " << fizzCount << endl;
    cout << "Buzz count : " << buzzCount << endl;
    cout << "FizzBuzz count: " << fizzBuzzCount << endl;

    

//task3
int y;
    cout << "Please enter a number between 3 and 9: ";
    cin >> y;

  
    if (y < 3 || y > 9) {
        cout << "Invalid input. Please enter a number between 3 and 9." << endl;
        return 0;
    }

    
    for (int i = 1; i <= y; i++) {
        for (int j = 1; j <= i; j++) {
            cout << "*";
        }
        cout << endl;
    }

    
    for (int i = y - 1; i >= 1; i--) {
        for (int j = 1; j <= i; j++) {
            cout << "*";
        }
        cout << endl;
    }

    return 0;
}
