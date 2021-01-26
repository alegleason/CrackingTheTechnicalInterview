
//  Created by Alejandro Gleason on 02/03/19.
//  Copyright © 2019 Alejandro Gleason. All rights reserved.
//  A01703013

import java.util.Scanner;

public class pony{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        long n;
        int asc = 0, rep = 0, flag = 0, pos = 0, flag2 = 0;
        n = sc.nextLong();

        //Creating and filling array
        long arr[] = new long [(int)n];
        for (int i=0;i<n;i++) {
            arr[i] = sc.nextLong();
        }

        for (int i =0;i < n-1 ;i++) {
            if (arr[i] > arr[i+1]) {
                rep++;
                break;//need to order
            }
        }

        if (rep==0) {
            System.out.println(rep);
            return;
        }

        for (int i =1; i < n; i++) {
            if (arr[i] < arr[i-1]) {
                flag++;//check each position on the array to see how much moves need to be made, if flag increments more than one time 
                pos=i;//save last position
            }
        }
        
        if(flag==1 && (arr[(int)n-1] <= arr[0])){
            System.out.println(n-pos);
            return;
        }else{//Imposible to order
            System.out.println(-1);
            flag2 = 1;
            //return;
        }

        if(flag2!=1){//flag2 serves as another validator, for the last if else
            for (int i = 0;i< n-1;i++) {//Ordered on ascending order, res would be n-1
                if (arr[i] < arr[i+1]) {
                asc++;//flag cant increment in this case
                break;
            }
        }

        if(asc==0){
            n=n-1;
            System.out.println(n);
            return;
        }
        return;
    }
}
}