//
//  main.cpp
//  678C
//
//  Created by Alejandro Gleason on 3/25/19.
//  Copyright © 2019 Alejandro Gleason. All rights reserved.
//

#include <iostream>
#include <algorithm>
#include <numeric>
using namespace std;

long long gcd (long long n1, long long n2) {//recursive version
    return (n2 == 0) ? n1 : gcd (n2, n1 % n2);
}

int main() {
    cin.tie(0);//for quickness
    ios_base::sync_with_stdio(0);
    long long n, a, b, p, q, atiles, btiles, ST, LCM, GCD, chocolates, mx;//n - tiles, a - for red tile, b - for blue tile, p - chcolates for red, q - chocolates for blue, atiles - red tiles, btiles - blue tiles, ST - same, LCM - less common multiplier, GCD - Greatest Common Divisor, chocolates - res, mx - max between p and q
    cin >> n >> a >> b >> p >> q;
    
    atiles = n/a; // this will indiscriminately give us all tiles that can be painted red
    btiles = n/b; //... and blue
    
    GCD = gcd(a, b); //calling the function for GCD
    //the LCM will help us calculate elements that can be painted either red or blue, since we will remove from the total of tiles that can be painted by blue or red, we need the LCM
    LCM=(a*b)/GCD; // least common multiplier  = (a*b)/greatest common divisor)
    
    ST = n/LCM; //st stands for same tiles, which are the tiles that can be painted both blue or red
    
    //removing common elements on red and blue
    atiles -= ST;
    btiles -= ST;
    
    //computing chocolate earning 
    atiles*=p;
    btiles*=q;
    
    mx = max(p,q);
    
    chocolates = atiles+btiles+(mx*ST); //since we removed common elements we have to consider them by multipling them by the max of p or q, ensuring the max
    
    cout << chocolates;
    
    return 0;
    
}
