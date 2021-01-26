//
//  main.cpp
//  155A
//
//  Created by Alejandro Gleason on 4/6/19.
//  Copyright © 2019 Alejandro Gleason. All rights reserved.
//

#include <iostream>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    int min=0, max=0,ans=0, aux;
    int n;
    cin >> n;
    int arr[n];
    
    
   /*for (int i = n-1; i>0; i--) {
        for (int j=i-1; j>=0; j--) {
            if (arr[j]<arr[i]) {
                min++;
            }else if(arr[j]>arr[i]){
                max++;
            }
        }
        if (min == i-1 || max == i-1) {
            ans++;
        }
        min = 0;
        max = 0;
    }
    
    max = arr[0];
    min = arr[0];
    
    for (int i = 0; i<n; i++) {
        aux = arr[i];
        
        
        //recalculate in each step min and max
        for (int j = i; j<n; j++) {
            if(arr[j] > max){
                max = arr[j];
            }
        }
        
        for (int j = i; j>0; j--) {
            if(arr[j] > min){
                min = arr[j];
            }
        }
        
        if(aux > max || aux < min){
            ans++;
        }
    }*/
    
   int val;
    
    cin >> val;
    
    min = val;
    max = val;
    
    for (int i = 1; i<n; i++) {
        cin>>val;
        if (val > max) {
            max = val;
            ans++;
        }else if(val < min){
            min = val;
            ans++;
        }
    }
    
    
    cout << ans;
    
    return 0;
}
