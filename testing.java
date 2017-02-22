import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Random rand=new Random();
        int t=rand.nextInt(6);
        System.out.println(t);
        int k;
        Set<Integer> input=new HashSet<Integer>();
        while(input.size()<t)
        {
            input.add(rand.nextInt(200-3+1)+3);
            
        }
        for(Integer n:input)
        {
            k=rand.nextInt(n-1+1)+1;
            System.out.println(n+" "+k);
            int ai;
            int max=10*10*10;
            int min=-10*10*10;
            for(int i=1;i<=n;i++)
            {
                ai=rand.nextInt((max-min)+1)+min;
                if(i%3==0){if(ai>0)ai=-1*ai;}
                else if(i%3==1){ai=0;}
                System.out.print(ai+" ");    
            }
            //ai=rand.nextInt((max-min)+1)+min;
            System.out.println();
            
        }
        
    }
}
