import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int Q = in.nextInt();
        for(int a0 = 0; a0 < Q; a0++)
        {
            int n = in.nextInt();
            String b = in.next();
            int j=0,k=0,i=0;
            Map<Character,Integer> map=new HashMap<Character,Integer>();
            char[] c=b.toCharArray();
            for(i=0;i<c.length;i++)
            {
                      if(c[i]!='_')
                      {  
                        if(map.get(c[i])==null)
                            map.put(c[i],1);
                        else
                            {
                                j=map.get(c[i])+1;
                                map.put(c[i],j);
                            }
                      }
                      else
                      {
                            k=-1;
                       }
            }
            for(char d:map.keySet())
            {
                    if(map.get(d)<2)
                    {
                        j=-1;
                        System.out.println("NO");
                                     break;
                    }
             }
            if(j!=-1 && k==-1 )
            {
                System.out.println("YES");
            }
            else if(j!=-1 && k==0)
            {
                if(c.length==2 && c[0]==c[1])System.out.println("YES");
                else{
                            for(i=1;i<c.length-1;i++)
                                { 
                                    if(c[i]!=c[i+1] && c[i]!=c[i-1])
                                    {
                                        System.out.println("NO");
                                        break;    
                                    }
                                }
                                if(i==c.length-1)
                                {
                                    System.out.println("YES");    
                                }

                     }
            }
            
         }
        
            
            
        
       
    }
}
