//
//  main.cpp
//  580A
//
//  Created by Alejandro Gleason on 4/6/19.
//  Copyright © 2019 Alejandro Gleason. All rights reserved.
//


#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int n,aux, ans = 1, maxx = 1, past = 1;//subsequence has min lentgh of 1
    cin >> n;
    int arr [n];
    
    for (int i = 0; i<n; i++) {
        cin >> aux;
        arr[i] = aux;
        if (i > 0) {
            if (arr[i] >= arr[i-1]) {//checking prev
                past++;
                ans = max(ans,past);
            }else{
                past=1;//reinitializing
            }
        }
    }
    cout << ans;
    return 0;
}
