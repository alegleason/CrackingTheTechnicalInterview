//
//  main.cpp
//  478C
//
//  Created by Alejandro Gleason on 1/26/19.
//  Copyright © 2019 Alejandro Gleason. All rights reserved.
//

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    //each group would at least have 2 diff. colors
    vector<long long> arr(3);
    long long res = 0;
    
    cin >> arr[0] >> arr[1] >> arr[2];//scan
    
    res = (arr[0] + arr[1] + arr[2])/3;//avg
    
    sort(arr.begin(), arr.end());//sort
    
    if(arr[0] + arr[1] < res){//res cant be bigger than the sumation of the smallest two numbers
        res = arr[0] + arr[1];
    }
    
    cout << res;
    
    return 0;
}
