//
//  main.cpp
//  441C
//
//  Created by Alejandro Gleason on 2/24/19.
//  Copyright © 2019 Alejandro Gleason. All rights reserved.
//

#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

int main() {
    //n are rows, m are columns and k are tubes
    int n, m, k, sizeTube, resTube, cellsPrinted = 0, cnt, i = 1;
    cin >> n >> m >> k;
    sizeTube = (n*m)/k; //size of each tube equals to rows per columns divided by the quantity of tubes
    cnt = sizeTube;//cnt stands for cells of each tube to be printed, works as a counter; it starts from the size of the tube
    resTube = (n*m)%k; //sometimes the size of the tubes wont adjust to the matrix, so we calcuate the reminder
    cout << sizeTube << " ";//printing the first component of the line
    for ( ; i <= n; i++) {//rove the matrix
        if(i%2!=0){//odd rows are roved from left to right, we start on odd rows (1)
            for (int j = 1; j <= m; j++) {
                cnt--;
                cellsPrinted++;
                cout << i << " " << j << " ";
                if (cnt<=0) {//this means we already filled one line, endl is needed as well as reinitializing our cnt
                    if (cellsPrinted + resTube == (n*m)) {
                        cnt = resTube;//this means we are only missing to print the reminder
                    }else{
                        cout << endl;
                        cnt = sizeTube;//reinitializing to print each tube
                        if(cellsPrinted + resTube + cnt == (n*m)){//here we calculate the size of the last tube
                            cnt = cnt + resTube;
                        }
                        if(cellsPrinted != n*m){//if we are still missing some cells to print, we /display again the size and start over
                            cout << cnt << " ";
                        }
                    }
                }
            }
        }
        if(i%2==0){//even rows are roved from right to left
            for (int j = m; j > 0; j--) {
                cnt--;
                cellsPrinted++;
                cout << i << " " << j << " ";//no need to add 1 to j
                if (cnt<=0) {
                    if (cellsPrinted + resTube == (n*m)) {
                        cnt = resTube;
                    }else{
                        cout << endl;
                        cnt = sizeTube;
                        if(cellsPrinted + resTube + cnt == (n*m)){
                            cnt = cnt + resTube;
                        }
                        if(cellsPrinted != n*m){
                            cout << cnt << " ";
                        }
                    }
                }
            }
        }
    }
    return 0;
}
