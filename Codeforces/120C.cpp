//
//  main.cpp
//  120C
//
//  Created by Alejandro Gleason on 9/15/19.
//  Copyright © 2019 Alejandro Gleason. All rights reserved.
//

#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int main(int argc, const char * argv[]) {
    int n, k, pigglet = 0, times, c;
    bool next = true;
    ifstream in;
    ofstream out;
    in.open("input.txt");
    out.open("output.txt");
    in >> n >> k; //Reading variables from file, saving them into n and k
    for (int i = 0; i < n; i++) {
        in >> c; //Reading capacity of jar
        int count = 0;
        next = true;
        while (next) {
            if (c < k || count == 3) {
                pigglet += c;
                next = false;
            }else{
                //cout << c << endl;
                c -= k;
                count++;
            }
        }
    }
    //cout << pigglet;
    out << pigglet; // Writing pigglet's honey
    in.close();
    out.close();
    return 0;
}
