//
//  main.cpp
//  230A
//
//  Created by Alejandro Gleason on 4/6/19.
//  Copyright © 2019 Alejandro Gleason. All rights reserved.
//

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int s, n;
    cin >> s >> n;
    //declaring vector of pairs
    vector< pair <int,int> > vect;
   // int st=2*n;
    int str[n];
    int bonus[n];
    for (int i = 0; i<n; i++) {
        cin >> str[i];
        cin >> bonus[i];
    }
    
    // Entering values in vector of pairs
    for (int i=0; i<n; i++){
        vect.push_back(make_pair(str[i],bonus[i]));
    }
    
    sort(vect.begin(), vect.end());
    
    for (int i = 0; i<n; i++) {
        if (s>vect[i].first) {
            s+=vect[i].second;
        }else{
            cout<<"NO";
            return 0;
        }
    }
    cout << "YES";
    return 0;
}
