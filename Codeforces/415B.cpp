//
//  main.cpp
//  415B
//
//  Created by Alejandro Gleason on 1/24/19.
//  Copyright © 2019 Alejandro Gleason. All rights reserved.
//


#include <iostream>

using namespace std;
int main() {
    int *a = NULL;
    int arr[3];
    
    for(int i=0;i<3;i++){
        cin>>arr[i];//n,a,b
    }
    
    
    int n = arr[0];
   
    a = new int[n];
    
    for(int i=0;i<a[0];i++){
        cin>>a[i];
    }
    
    int res[a[0]];
    
    for(int i=0;i<a[0];i++){
        res[i] = (arr[i]*a[1])%a[2];
    }
    
    for(int i=0;i<a[0];i++){
        cout<<res[i];
    }
    
    delete [] a;
    a = NULL;
    
    return 0;
}

