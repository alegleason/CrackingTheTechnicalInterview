//
//  main.cpp
//  450B
//
//  Created by Alejandro Gleason on 4/6/19.
//  Copyright © 2019 Alejandro Gleason. All rights reserved.
//

#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    ios_base::sync_with_stdio (true);//quickness
    long int x, y, n, arr[6], actual, res, mod;
    cin >> x >> y >> n;
    //position given
    long int pos=n%6;
    //formula to follow: f1=x, f2=y, forall i(i>=2), fi = fi-1 + fi+1
    arr[1]=x; //one based index
    arr[2]=y;
    for (int i = 3; i<7; i++) {//filling missing positions
        //following the formula
        actual=y-x;
        //moving positions
        x = y;
        y = actual;
        arr[i%6] = y;
    }
    //with filled array
    
    
    mod = arr[pos];
    
    res = ((mod%1000000007)+1000000007)%1000000007;//ensuring limits
    
    cout << res;
    
    //In the second sample, f2 =  - 1;  - 1 modulo (109 + 7) equals (109 + 6) ---> using the 6 as key

    return 0;
}
