//
//  main.cpp
//  519B
//
//  Created by Alejandro Gleason on 10/26/19.
//  Copyright © 2019 Alejandro Gleason. All rights reserved.
//

#include <iostream>
#include <set>

using namespace std;

int main(int argc, const char * argv[]) {
    ios::sync_with_stdio(true);//quickness
    int n, aux = 0, error1 = 0, error2 = 0;
    long int sum = 0, prevSum = 0, c = 0, aux2, iter; //sum stands for the current stage sum, and prevSum is for the previous stage sum
    cin >> n;
    iter = n - 2; //only 3 possible stages, t, t-1 and t-2
    
    while (n >= iter) { /*keep into limits*/
        n--; //Going one it up, could go up?
        for (int i = 1; i <= (n+1); i++) {
            //Adding all values
            cin >> aux;
            sum = sum + aux;
        }
        /*first time*/
        if (c == 0) {
            prevSum = sum;
        }else{
            //missing value is gotten with this simple operation
            aux2 = prevSum - sum;
            cout << aux2 << endl;
            prevSum = sum;
        }
        sum = 0;
        c++;
    }
    return 0;
}
