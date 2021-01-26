//
//  main.cpp
//  816B
//
//  Created by Alejandro Gleason on 9/24/19.
//

#include <iostream>
#include <iterator>
#include <map>

using namespace std;

typedef long long ll;

int main() {
    ll n, k, q, min = 0, max = 0, aux1, aux2, temp, first, second, count = 0;
    map<ll, pair<ll,ll>> temperatures; /* Map that stores the temperatures, key is just an integer */
    map<ll,ll> times;  /* Map that stores the times, key is the temperature */
    map<ll, pair<ll,ll> > ::iterator it;
    map<ll, ll> ::iterator itt;
    map<ll, ll> ::iterator itt2;
    it = temperatures.begin();
    /* 'n' is the number of recipes 'k' is the minimum to be approved 'q' are the questions */
    cin >> n >> k >> q;
    for (ll i = 0; i < n; i++) {
        cin >> aux1 >> aux2;
        /* Setting initial values, for min and max */
        if (i == 0) {
            min = aux1;
            max = aux2;
        }
        /* Inserting temperatures and updating min and max */
        temperatures.insert(it, {i, pair<ll,ll>(aux1, aux2)});
        if (aux1 > max) {
            max = aux1;
        }
        if (aux2 > max) {
            max = aux2;
        }
        if (aux1 < min) {
            min = aux1;
        }
        if (aux2 < min) {
            min = aux2;
        }
    }
    
    itt = times.begin();
    temp = min;
    for (ll i = 0; i <= max-min; i++, temp++) {
        times.insert(itt, {temp, 0});
    }
    
    itt=times.begin();
    itt2=times.begin();
    
    /* Filling with occurences */
    
    for (it = temperatures.begin(); it != temperatures.end(); it++) {
        first=it->second.first;
        second=it->second.second;
        /* Returns location and adds their count */
        itt=times.find(first);
        itt2=times.find(second);
        /* Updating the counter associated with each temperature, that works as key */
        for (; itt != itt2; itt++) {
            itt -> second++;
        }
         itt -> second++;
    }
    
    /* Printing the map with values
    
    itt = times.begin();
    for (; itt != times.end(); itt++) {
        cout << itt->first << " " << itt->second << endl;
    } */
    
    /* Logic using q and k */
    
    for (ll i = 0; i < q; i++) {
        cin >> aux1 >> aux2;
        count = 0;
        itt = times.begin();
        itt2 = times.begin();
        for (ll j = aux1; j < aux2+1; j++) {
            //cout << "j vale" << j << endl;
            itt = times.find(j);
            if(!(itt == times.end())){
                if ((itt -> second) >= k){
                    count++;
                }
                
            }
        }
        cout << count << endl;
    }
    
    return 0;
}
