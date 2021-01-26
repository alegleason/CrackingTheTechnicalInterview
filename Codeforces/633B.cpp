//
//  main.cpp
//  633B
//
//  Created by Alejandro Gleason on 20/10/18.
//  Copyright © 2018 Alejandro Gleason. All rights reserved.
//

#include <iostream>
#include <vector>
using namespace std;
//https://www.geeksforgeeks.org/count-trailing-zeroes-factorial-number/

int findTrailingZeros(int n)
{
    // Initialize result
    int count = 0;
    // Keep dividing n by powers of 5 and update count
    for (int i = 5; n / i >= 1; i *= 5)
        count = (n / i) + count;//(n/i) can just give as a result 0 or 1
    return count;
}

int main() {
    vector<int> res;
    int m, count = 0;
    cin >> m;
    for(int i=0; i<(m+1)*5; i++){
        if (findTrailingZeros(i) == m) {
            res.push_back(i);
            count++;
        }
    }
    cout << count << "\n";
    if (!res.empty()) {
        for (int i = 0; i < res.size(); i++){
            cout << res[i] << " ";
        }
    }
    return 0;
}
