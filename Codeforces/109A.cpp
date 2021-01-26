//
//  main.cpp
//  109A
//
//  Created by Alejandro Gleason on 2/23/19.
//  Copyright © 2019 Alejandro Gleason. All rights reserved.
//

#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, flag = 0;
    vector<int> v;
    cin >> n;
    if(n<4){//basic cases
        cout << "-1";
        return 0;
    }else if(n == 4){
        cout << "4";
        return 0;
    }else if(n==7){
        cout << "7";
        return 0;
    }
    for (int i = n/7; i>=0; i--) {//achieve as many sevens as posible
        int res = n - (i*7);//getting the reminder of n
        if (res%4 == 0) {//check if the reminder is a multiple of 4
            flag = 1;
            for (int j = 0; j<res/4; j++) {//adding the fours needed
                v.push_back(4);
            }
            for (int k = 0; k<i; k++) {//adding the sevens needed
                v.push_back(7);
            }
            break;
        }
    }
    if(flag != 1) {
        cout<< "-1";
    }else{
        for (int i = 0; i < v.size(); i++) {
            cout << v[i];
        }
    }
    return 0;
}
