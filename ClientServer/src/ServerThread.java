import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;


public class ServerThread extends Thread{
	Socket socket;
	public ServerThread(Socket socket)
	{
		this.socket=socket;
	}
	public void run()
	{
		try{
		String message=null;
		BufferedReader b=new BufferedReader(new InputStreamReader(this.socket.getInputStream()));
		while((message=b.readLine())!=null)
		{
			System.out.println("Incoming message from  "+message);
			PrintWriter p=new PrintWriter(socket.getOutputStream(),true);
			p.println("Server said Thanks for the message "+message);
			
		}
		
		}catch(IOException e){System.out.println("exception"+e);}
	}
}
