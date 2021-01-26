//
//  main.cpp
//  755B
//
//  Created by Alejandro Gleason on 10/8/19.
//  Copyright © 2019 Alejandro Gleason. All rights reserved.
//

#include <iostream>
#include <map>
#include <set>
using namespace std;

int main(int argc, const char * argv[]) {
    string sAux;
    long n, m, commons, total, size; /*Commons is the number of words that were repeated by both balls*/
    set<string> stringSet;
    
    cin >> n >> m;
    
    total = n + m; /*All words*/
    
    for(int i = 0; i < total; i++)
    {
        cin>>sAux; /*Filling a set with all strings*/
        stringSet.insert(sAux);
    }
    
    size = stringSet.size();
    
    commons = total - size;
    if(commons > 0){
        /*There are commons, otherwise, commons would be equal to 0*/
        
        n = n - commons; /*actual n's*/
        m = m - commons; /*actual m's*/
        
        if(commons%2 == 1){ /*That means n will have one more word*/
            /*Dividing by two because commons belong to both balls*/
            n = n + (commons)/2 + 1;
            m = m + (commons)/2;
        } else {/*Each ball will say the same amount of words*/
            n = n + (commons)/2;
            m = m + (commons)/2;
        }
    }
    
    //cout << n << m << size << endl;
    
    if(n>m){
        cout << "YES" << endl;
    }
    else{
        cout << "NO" << endl;
    }
    
    return 0;
}
