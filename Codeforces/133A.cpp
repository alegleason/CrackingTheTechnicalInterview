//
//  main.cpp
//  PROJ
//
//  Created by Alejandro Gleason on 4/6/19.
//  Copyright © 2019 Alejandro Gleason. All rights reserved.
//

#include <iostream>
using namespace std;

int main() {
    char arr[101];
    int flag = 0;
    string s;
    cin >> s;
    
    for (int i = 0; i < s.length(); i++) {
        if (s.at(i) == 'H' || s.at(i) == 'Q' || s.at(i) == '9') {
            cout << "YES";
            return 0;
        }else{
            flag = 1;
        }
    }
    
    if (flag == 1) {
        cout << "NO";
    }
    return 0;
}
