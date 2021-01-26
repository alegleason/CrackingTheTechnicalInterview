//
//  main.cpp
//  723A
//
//  Created by Alejandro Gleason on 4/6/19.
//  Copyright © 2019 Alejandro Gleason. All rights reserved.
//

#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int c1, c2, c3;
    int arr[3];
    for (int i = 0; i<3; i++) {
        cin >> arr[i];
    }
    sort(arr, arr+3);
    
    c1 = abs(arr[2]-arr[1]);
    c2 = arr[1]-arr[0];
    c3=c1+c2;
    cout <<  c3;
    
    return 0;
}
