
public class Fibonacci
{
	public static void main(String[] args)
	{int n=0;
		while(n<=12)
		{
			System.out.println(new Fibonacci().fibonacci(n));
			n++;
		}
		
		new Fibonacci().mulTable(12);
		new Fibonacci().printOdd();
		
		
	}
		public int fibonacci(int n)
	 {
//		if(n==1|n==2)
//			return n-1;
//		else
//			return fibonacci(n-1)+fibonacci(n-2);
			return n<=1?n:fibonacci(n-1)+fibonacci(n-2);
		
		
	}

		public void mulTable(int n)
		{
			for(int i=1;i<=n;i++){
				for(int j=1;j<=n;j++)
				{
					System.out.print(i*j+" ");
				}
				System.out.println();
			}
		}
		
		public void printOdd()
		{
			for(int i=1;i<=99;i++){
			System.out.print(i%2==1?Integer.toString(i):" ");
			
			}
		}
}
