//
//  main.cpp
//  842B
//
//  Created by Alejandro Gleason on 20/10/18.
//  Copyright © 2018 Alejandro Gleason. All rights reserved.
//

#include <iostream>
#include <math.h>
using namespace std;

int main() {
    int R, d, n;//outer circle and number of salamis
    int xi, yi, ri, count = 0;
    int pyth;
    cin >> R >> d;
    int aux = R - d;//aux = inner circle
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> xi >> yi >> ri;
        pyth = (xi*xi) + (yi*yi);
        pyth = sqrt(pyth);
        if ((pyth >= (aux+ri)) && ((pyth+ri) <= R)) {//If it is outside the inner circle, and inside the outer circle...
            count++;
        }
    }
    cout << count;
    return 0;
}
