import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Random rand=new Random();
        int t=5;
        System.out.println(t);
        int k;
        Set<Integer> input=new HashSet<Integer>();
        while(input.size()<t)
        {
            input.add(rand.nextInt(200-3+1)+3);
            
        }
        int count=0;
        for(Integer n:input)
        {
            count++;
            k=rand.nextInt(n-1+1)+1;
            System.out.println(n+" "+k);
            int ai;
            int max=10*10*10;
            int min=-10*10*10;
            for(int i=1;i<=n;i++)
            {
                ai=rand.nextInt((max-min)+1)+min;
                if(count%2==0)
                {
                    if(i<k && ai>0)ai=-1*ai;
                    if(i==k)ai=0;
                    if(i>k && ai<0)ai=ai*-1;
                }
                else
                {   if(i==1)ai=0;
                    else if(i==2)ai=-1;
                    else if(ai<0)ai=-1*ai;
                    
                }
                System.out.print(ai+" ");    
            }
            //ai=rand.nextInt((max-min)+1)+min;
            System.out.println();
            
        }
        
    }
}
