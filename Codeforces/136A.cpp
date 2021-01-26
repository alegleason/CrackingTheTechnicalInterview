//
//  main.cpp
//  Presents
//
//  Created by Alejandro Gleason on 2/7/19.
//  Copyright © 2019 Alejandro Gleason. All rights reserved.
//

#include <iostream>
using namespace std;

int main() {
    int n, pi;
    cin >> n;
    //Creating array
    int arr[n+1];
    //Scanning pi's
    for (int i = 1; i <= n; i++)
    {
        cin >> pi;
        arr[pi] = i;//moving to the correct friend
    }
    
    for (int i = 1; i <= n; i++)
    {
        cout << arr[i] << " ";
    }
    return 0;
}
