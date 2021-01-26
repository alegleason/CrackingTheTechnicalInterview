//
//  main.cpp
//  10324UVA
//
//  Created by Alejandro Gleason on 2/10/19.
//  Copyright © 2019 Alejandro Gleason. All rights reserved.
//

#include <iostream>
using namespace std;
int main() {
    string s;
    int n, i, j;
    cin >> s;
    cin >> n;
    bool flag=true;
    while (n > 0) {
        flag=true;
        cin >> i >> j;
        if (i == j) {
            cout << "YES";
        }else if (i < j){
            for (; i < j; i++) {
                if(s[i] != s[j]){
                    flag=false;
                    break;
                }
            }
        }else if(i > j){
            for (; i > j; j++) {
                if(s[j] != s[i]){
                    flag=false;
                    break;
                }
            }
        }if (flag==true){
            cout << "YES\n";
        }else if (flag==false){
            cout << "NO\n";
        }
        n--;
    }
    
    return 0;
}
