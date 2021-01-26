//
//  main.cpp
//  268C
//
//  Created by Alejandro Gleason on 3/22/19.
//  Copyright © 2019 Alejandro Gleason. All rights reserved.
//
// For this problem, to get the maximum number of pairs I lean on the pigeons theorem, which says that if n doves are distributed on m dovecotes, and if n > m, then it will be at least a dovecote with more than one dove. https://es.wikipedia.org/wiki/Principio_del_palomar. So the max. number of pairs would be the min number of 'n' or 'm' + 1.

#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int n, m, pt;//pt stands for pidgeons theorem
    cin >> n >> m;
    
    //not used... (better to have each case uniquely)
    //pt = min(n, m);
    //pt += 1;
    //cout << pt << endl;
    
    // We will use the formula for the distance between two points, which is square root based, ensuring non integers. https://orion.math.iastate.edu/dept/links/formulas/form2.pdf
    
    if(n == m) { // si n y m son iguales
        cout << n+1 << endl;
        // The principle follows that we can increase on x (which starts on 0) and decrease on y, which starts on m, while y is bigger than 0 (non negatives), since x+y>0.
        for(int x = 0, y = m; y >= 0; x++, y--){
            cout << x << " " << y << endl;
        }
    } else if(n < m) {
        pt = min(n+1, m);
        cout << pt << endl;
        for(int x = 0, y = m; x <= n; x++, y--){
            cout << x << " " << y << endl;
        }
    } else if(n > m) {
        // we cant print directly m+1 bc there can be the case that m+1 is greater or equal to n, which was initially smaller
        pt = min(n, m+1);
        cout << pt << endl;
        for(int x = 0, y = m; y >= 0; x++, y--){
            cout << x << " " << y << endl;
        }
    } else{
        cout << -1; // Unsolvable (?)
    }
    
    return 0;
}
