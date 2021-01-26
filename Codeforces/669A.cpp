//
//  main.cpp
//  669A
//
//  Created by Alejandro Gleason on 3/8/19.
//  Copyright © 2019 Alejandro Gleason. All rights reserved.
//

#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int n, prevN = 1, res = 0;
    cin >> n;
   /*if(n==1){
        cout << 1;
        return 0;
    }else if(n==2){
        cout << 1;
        return 0;
    }else if(n==3){
        cout << 2;
        return 0;
    }*/
    while(n > 0){
        if(prevN == 1){
            n-=prevN;
            prevN = 2;
            res++;
            if(n==1){//This means we cant advance
                cout << res;
                return 0;
            }
        }else if(prevN == 2){
            n-=prevN;
            prevN = 1;
            res++;
        }
    }
    cout << res;
    return 0;
}
