//
//  main.cpp
//  25A
//
//  Created by Alejandro Gleason on 4/6/19.
//  Copyright © 2019 Alejandro Gleason. All rights reserved.
//

#include <iostream>
using namespace std;

int main() {
    int n,aux,mod1=0,mod2, indI=0, indP=0;
    cin >> n;
    /*int arr[n];
    for (int i = 0; i<n; i++) {
        cin >> aux;
        arr[i] = aux;
    }
    
    for (int i = 0; i<n; i++) {
        cin >> aux;
        arr[i] = aux;
    }*/
    for (int i = 1; i<=n; i++) {//1 based index for answer
        cin >> aux;
        if (aux%2==0) {
            mod1 +=1;
            indP = i;//saving the index, pair
        }else{
            mod1 -= 1;
            indI = i;//not pair
        }
    }
    if (mod1 > 0) {
        cout << indI;
    }else{
        cout << indP;
    }
    return 0;
}
