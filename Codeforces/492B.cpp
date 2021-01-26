//
//  main.cpp
//  492B
//
//  Created by Alejandro Gleason on 4/6/19.
//  Copyright © 2019 Alejandro Gleason. All rights reserved.
//

#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int lint, calle;
    cin >> lint >> calle;
    int cal=lint+2;
    int arr[cal];
    arr[0] = 0;
    
    for (int i = 1; i<lint+1; i++) {
        cin >> arr[i];
    }
    
    
   arr[lint+1]=calle;
    
   //cout << calle;
    
    sort(arr, arr+(lint+1));
    
    //for (int i = 0; i<lint+1; i++) {
       // cout << arr[i] << " ";
    //}
    
    //cout << endl;
    
    int max = 0;
    
    for (int i = 1; i < lint+1; i++) {
        if ((arr[i+1]-arr[i])>max) {
            int n =arr[i+1]-arr[i];
            max=n;
            
        }
        //cout << "diff is: " << arr[i+1]-arr[i]<< endl;
    }
    
   // cout << max <<endl;
    
    if (arr[1] == 0) {
        double res;
        
        res = max/2.00;
        
        cout << res;
    }else{
        int newdif = arr[1];
        if (newdif > (max) {
            double res;
            
            res = newdif;
            
            cout << res;
        }else{
            
        }
        cout
    }
    
    return 0;
}
