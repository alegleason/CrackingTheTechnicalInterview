//
//  main.cpp
//  834B
//
//  Created by Alejandro Gleason on 8/25/19.
//  Copyright © 2019 Alejandro Gleason. All rights reserved.
//


#include <iostream>
#include <iterator>
#include <map>
#include <set>
//sets can't contain repeated elements, maps neither, but they use keys

using namespace std;

int main() {
    map<char, int> last_pos;//map of last pos, key is the letter, it has associated an int that indicates the last occurence position
    set<char> active;//set of active letters, just contains letters that are active and has its control
    int guests, guards;
    cin >> guests >> guards;
    string order;
    cin >> order;
    
    //determine last position of letters
    for (int i = 0; i < guests; i++) {
            last_pos[order[i]] = i;
    }
    
    for (int i = 0; i < guests; i++) {
        //insert the letter into actives, if it cant be inserted bc its already there, there is no problem!
        active.insert(order[i]);
        //no more active letters at any time can be bigger than the guards
        if (active.size() > guards) {
            cout << "YES" << endl;
            return 0;
        }
        //if we get to the last position of a letter, we erase it from active
        if (last_pos[order[i]] == i)
            active.erase(order[i]);
    }
    
    cout << "NO" << endl;
    return 0;
}
