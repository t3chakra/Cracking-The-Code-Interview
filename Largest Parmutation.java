import java.io.*;
import java.util.*;

public class Solution {
   

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner in=new Scanner(System.in);
        int n=in.nextInt();
        int k=in.nextInt();
        int[] arr=new int[n];
        int max=-99999;
        int maxIn=0;
        int temp;
        int[]index=new int[n+1];
        for(int i=0;i<n;i++){arr[i]=in.nextInt();index[arr[i]]=i;}
        //for(int i=0;i<n+1;i++)System.out.println("index["+i+"] "+index[i]);
        for(int i=0;i<n;i++)
        {
            if(k==0)break;
            if(arr[i]!=n-i)
            {
                temp=index[n-i];
                arr[temp]=arr[i];//taking 2 to position of 8
                index[n-i]=i;
                index[arr[i]]=temp;
                arr[i]=n-i; //taking 8 to position of 2
                k--;
                
                
            }
            
        }
     
        
        for(int i=0;i<n;i++){System.out.print(arr[i]+" ");}
        
        
    }
}
