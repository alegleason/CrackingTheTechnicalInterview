//
//  main.cpp
//  701B
//
//  Created by Alejandro Gleason on 9/15/19.
//  Copyright © 2019 Alejandro Gleason. All rights reserved.
//

#include <iostream>
#include <stdio.h>

using namespace std;

long long n, m, cells[100005], xcnt, ycnt, x[100005], y[100005], aux;

int main()
{
    //long long n,m,ans[100005],r[100005],c[100005],x,y;
    scanf("%I64d%I64d",&n,&m);
    //Originally xcnt*ycnt would give the total available cells, so we assume that
    xcnt = n;
    ycnt = n;
    //Declaring x and y arrays, will save its coordinates
    for(int i=1;i<=m;i++){
        int xCord, yCord;
        scanf("%d%d",&xCord,&yCord);
        if(!x[xCord]){ //Not occupied
            x[xCord]=1; //Marked it as occupied
            xcnt--; //Delete all row
        }
        if(!y[yCord]){
            y[yCord]=1;
            ycnt--;//Delete all column
        }
        cells[i]=xcnt*ycnt;//Calculate new available cells
        aux=xcnt*ycnt;
        printf("%I64d ",aux);
        //cout << cells << " ";
    }
   /* for(int i=1;i<m;i++){
        printf("%I64d ",cells[i]);
        //cout << cells[i] << " ";
    }
    printf("%I64d\n",cells[m]);
    //cout << cells [m] << " ";*/
    return 0;
}


