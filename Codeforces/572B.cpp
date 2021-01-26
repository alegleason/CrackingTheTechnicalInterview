//
//  main.cpp
//  844B
//
//  Created by Alejandro Gleason on 10/26/19.
//  Copyright © 2019 Alejandro Gleason. All rights reserved.
//

#include<iostream>
#include<algorithm>
#include<vector>
#include<map>

using namespace std;

int main() {
    int i, k, n, s, p, q;
    char ch;
    
    /*n is number of orders and s is book depth*/
    cin >> n >> s;
    /*maps for orders, one for buy and one for sell*/
    map<int,int> buy;
    map<int,int> sell;

    /*aggrupation is made automatically by maps*/
    for(i=0; i<n; i++)
    {
        /*scanning 'buy/sell', price and direction*/
        cin >> ch >> p >> q;
        /*associate price with direction, in buy map*/
        if(ch == 'B'){
            buy[p] += q;
        }
         /*associate price with direction, in sell map*/
        else if (ch == 'S'){
            sell[p] += q;
        }
    }
    
    /*vectors (order book) that contain aggregated orders, contains buy orders also sorted by price in descending order*/
    vector<pair<int,int>> vectorBuy;
    /*contains (order book) sell orders sorted by price in descending order*/
    vector<pair<int,int>> vectorSell;
    
    /*iterator to move in buy*/
    map<int,int>:: iterator it1=buy.begin();
    /*move through all the map*/
    while(it1!=buy.end())
    {
        /*associate it to buy order book*/
        vectorBuy.push_back({it1->first,it1->second});
        it1++;
    }
    
    /*iterator to move in sell*/
    it1=sell.begin();
    /*move through all the map*/
    while(it1!=sell.end())
    {
         /*associate it to sell order book*/
        vectorSell.push_back({it1->first,it1->second});
        it1++;
    }
    
    /*both type of orders must be sorted in descending order, but sell orders will be first sorted in ascending so we eliminate the ones that have higher price, to meet quality criteria.*/
    /*A buy order is better if it has higher price and a sell order is better if it has lower price.*/
    sort(vectorSell.begin(), vectorSell.end());
    sort(vectorBuy.begin(), vectorBuy.end(), greater<pair<int,int>>()); /*descending*/

    /*throw the extras, most expensive from sell*/
    while(vectorSell.size() > s){
        vectorSell.pop_back();
    }
    
    /*throw the extras, most cheap from buy*/
    while(vectorBuy.size() > s){
        vectorBuy.pop_back();
    }
    
    /*actually sorting sell in descending*/
    sort(vectorSell.begin(), vectorSell.end(), greater<pair<int,int>>());
    
    /*printing orders*/
    i=0;
    while(i < vectorSell.size() )
    {
        cout << "S " << vectorSell[i].first << " " << vectorSell[i].second << endl;
        i++;
    }

    i=0;
    while(i < vectorBuy.size())
    {
        cout << "B " << vectorBuy[i].first << " " << vectorBuy[i].second << endl;
        i++;
    }

    return 0;
}
