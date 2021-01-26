//
//  main.cpp
//  490C
//
//  Created by Alejandro Gleason on 4/6/19.
//  Copyright © 2019 Alejandro Gleason. All rights reserved.
//

#include <iostream>
#include <cstring>
#include <algorithm>
#define FOR(i,a,b) for(int i=a;i<=b;i++)//normal for
#define DFOR(i,a,b) for(int i=a;i>=b;i--)//reverse for
#define MAX 1000111
using namespace std;
//define all outside so segmentation fault is not a problem: https://stackoverflow.com/questions/12762944/segmentation-fault-11
char num[MAX];//array of chars, since we will perform moving operations
int a, b;
int aux[MAX];//where we will do actual calculations, left side
int aux2[MAX];//right side

int main() {
    std::ios::sync_with_stdio(true);//quickness
    int size;
    scanf("%s",num);//for access to locations
    cin >> a >> b;
    size = strlen(num);
    if (num[0]=='0') {//case 0
        cout << "NO"<<endl;
        return 0;
    }
    
    aux[0]=0;//pr
    FOR(i,1,size){//a part
        aux[i]=(aux[i-1]*10+num[i-1]-'0')%a;//converting to an actual num
    }
    /*for (int i = 1; i<=size; i++) {
        
    }*/
    
    aux2[size+1]=0;
    int p = 1;
    DFOR(i,size,1){//b part, reversed for
        aux2[i]=(aux2[i+1]+p*(num[i-1]-'0'))%b;//converting to an actual num
        p=(p*10)%b;//10 pows
    }/*for (int i = size; i>=1; i--) {
        
    }*/
    
    FOR(i, 1, size-1){
        if (num[i]!='0') {//so it does not takes zero as a possible option
            if((aux[i]==0) && (aux2[i+1]==0)){//checking for valid answers
                cout<<"YES"<<endl;
                FOR(cs, 1, i){//getting ans
                    cout<<num[cs-1];
                }
                //for (int cs = 1; cs<=i; cs++) {//a
                
                //}
                cout<<endl;
                FOR(cs, i+1, size){
                    cout<<num[cs-1];
                }
                //for (int cs= i+1; i<=size;i++) {//b
                
                //}
                cout<<endl;
                return 0;//exiting
            }
        }
    }
   /* for (int i = 1; i<(size-1); i++) {
        if (num[i]!=0) {
            
        }
    }*/
    
    cout<<"NO"<<endl;
    
    return 0;
}
