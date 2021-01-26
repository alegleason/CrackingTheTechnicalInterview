//
//  main.cpp
//  478B
//
//  Created by Alejandro Gleason on 2/23/19.
//  Copyright © 2019 Alejandro Gleason. All rights reserved.
//

#include <iostream>
using namespace std;

int main() {
    long long m, n, kmax, kmin, reminder;
    //n are participants, m are teams
    cin >> n >> m;
    //FOR MAX
    kmax = n-m+1;//number of maximum people in one team after supposing we assign one member to each other team
    
    kmax = kmax*(kmax-1)/2; //mathematic formula n(n-1)/2 is used to get the number of pairings (1 way pairings)
    
    //FOR MIN
    //uniform teams (teams of the same number of members)
    kmin = (n/m) * ((n/m)-1)/2;//positive pairings
    //for minimum number you would like to have equal number of people in all groups, so first you give n/m members to each team
    kmin = kmin*(m-(n%m));//n%m is the remainder, so we dont take it into account
    reminder = (n/m) * ((n/m)+1)/2; //pairing the reminder of uniform teams, now considering them
    kmin = kmin + reminder*(n%m);//kmin is the sum of the positive pairings plus the parings of the reminders multiplied by the actual reminder
    
    cout << kmin << " " << kmax;
    return 0;
}
