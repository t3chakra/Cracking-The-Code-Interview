import java.util.Scanner;
public class Reverse {

	public static void main(String[]args)
	{
		Scanner in=new Scanner(System.in);
		String s=in.nextLine();
		int l=s.length();
		int last=l-1;
		char []ch=s.toCharArray();
		for(int i=0;i<l/2;i++)
		{
			char c=ch[last-i];
			ch[last-i]=ch[i];	
			ch[i]=c;
		System.out.println(new String(ch));
			
			
		}//System.out.println(new String(ch));		
		
		in.close();
		
	}
}
