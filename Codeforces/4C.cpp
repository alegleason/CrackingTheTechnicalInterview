//
//  main.cpp
//  4C
//
//  Created by Alejandro Gleason on 8/25/19.
//  Copyright © 2019 Alejandro Gleason. All rights reserved.
//

#include <iostream>
#include <iterator>
#include <map>

using namespace std;

//idea: use map to get response, if it exists then concat + 1, if not, print OK

int main() {
    int num;
    string nom;
    map<string, int> reg;//registered people, database
    
    cin >> num;
    
    for (int i = 0; i<num; i++) {
        cin >> nom;
        if(reg.insert(make_pair(nom, 0)).second == true)
        {
            cout << "OK" << endl;
        }else{//using nom as key, it is on the column of key
            cout << nom << reg[nom] << endl;
        }
        reg[nom]++;
    }
    
    return 0;
}
