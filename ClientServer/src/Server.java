import java.io.IOException;
import java.net.*;


public class Server
{
	public static final int PORT=4444;
	public static void main(String[] args) throws IOException
	{	
		new Server().runServer();
	}
	public void runServer() throws IOException{
		
		try{
			ServerSocket serverSocket=new ServerSocket(PORT);
			System.out.println("Server up and ready for connection");
			while(true)
			{
				Socket socket=serverSocket.accept();
				new ServerThread(socket).start();
			}
			
		}
		catch(Exception e){System.out.println("exception"+e);}
	}
}
