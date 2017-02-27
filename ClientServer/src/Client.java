import java.io.*;
import java.net.*;
import java.util.Scanner;
public class Client {
	public static void main(String args[])
	{
		
		if (args.length>0){
		try{
			String name=args[0];
			Socket socket=new Socket("192.168.1.14",4444);
			
			PrintWriter p=new PrintWriter(socket.getOutputStream(),true);
			BufferedReader b=new BufferedReader(new InputStreamReader(System.in));
			BufferedReader b2=new BufferedReader(new InputStreamReader(socket.getInputStream()));
			
			while(true){
				System.out.println("Enter Your message");
				p.println(name+" : "+ b.readLine());
				System.out.println(b2.readLine());
				
			}
		}
		catch(Exception e){System.out.println("Exception"+e);}
	}
	else{System.err.println("Usage: Client <server> <name>");}
	}
}
