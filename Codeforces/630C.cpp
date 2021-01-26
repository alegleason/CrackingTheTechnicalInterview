//
//  main.cpp
//  630C
//
//  Created by Alejandro Gleason on 9/15/19.
//  Copyright © 2019 Alejandro Gleason. All rights reserved.
//
// http://jonisalonen.com/2013/calculating-combinations/

#include <iostream>
#include <math.h>       /* pow */
using namespace std;

long long arr [56]; //Global arr

void fill();

int main() {
    int n;
    cin >> n;
    fill(); // Filling the array
    long long res = arr[n];
    cout << res;
    return 0;
}

void fill() { //Fills the array of lucky numbers
    arr[0] = 0;
    arr[1] = 2; //Can only have 7 and 8. One based index.
    arr[2] = 6; //7, 8, 77, 88, 78, 87
    for (int i = 3; i<=55; i++) {
        int aux = pow(2,i); // 2 to the i will give me the combinations of two numbers at with n possible positions, if we had three numbers, we would just have to change 2
        //cout << aux << endl;
        //cout << pow(2, i);
        arr[i] = arr[i-1] + pow(2,i); // previous location + calculated
    }
}
