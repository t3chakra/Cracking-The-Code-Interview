import java.util.Scanner;
class TreeNode{
	int data;
	TreeNode left;
	TreeNode right;
	public TreeNode(int data)
	{
		this.data=data;
		this.left=null;
		this.right=null;
	}
	public boolean insert(int data)
	{
		if(this.data==data){return false;}
		else{
			if(data<this.data)
			{
				if(this.left==null)
				{
					this.left=new TreeNode(data);
					return true;
				}
				else 
					return this.left.insert(data);
			}
			else
			{
				if(this.right==null)
				{
					this.right=new TreeNode(data);
					return true;
				}
				else
					return this.right.insert(data);
			}
		}
		
	}
	public boolean find(int data)
	{
		if(this.data==data){
			return true;
		}
		else if(data<this.data)
		{
			 if(this.left!=null)
				return this.left.find(data);
			else 
				return false;
		}
		else{
			 if(this.right!=null)
					return this.right.find(data);
				else 
					return false;
		}
		
	}
	public void inOrder()
	{
		if(this.left!=null)
			this.left.inOrder();
		System.out.println(this.data);
		if(this.right!=null)
			this.right.inOrder();
	}
	public void postOrder()
	{
		if(this.left!=null)
			this.left.postOrder();
		if(this.right!=null)
			this.right.postOrder();
		System.out.println(this.data);
	}
	public void preOrder()
	{
		System.out.println(this.data);
		if(this.left!=null)
			this.left.preOrder();
		if(this.right!=null)
			this.right.preOrder();
		
	}
	
}
class Tree
{
	TreeNode root;
	public Tree(){
		this.root=null;
	}
	public boolean insert(int data)
	{
		if(this.root==null)
		{
			this.root=new TreeNode(data);
			return true;
			
		}
		else
		{
			return this.root.insert(data);
		}
		
	}
	public boolean find(int data)
	{
		if(this.root==null)
		{
				return false;
		}
		else
			return this.root.find(data);
	}
	public void inOrder()
	{
		System.out.println("Inorder");
		this.root.inOrder();
	}
	public void preOrder()
	{
		System.out.println("Pre-order");
		this.root.preOrder();
	}
	public void postOrder()
	{
		System.out.println("Post-order");
		this.root.postOrder();
	}
	
}
public class BinarySearchTree 
{
	public static void main(String[] args)
	{
		
		Tree  btree=new Tree();
		Scanner in=new Scanner(System.in);
		System.out.println(" Enter the size of the tree");
		int size=in.nextInt();
		for(int i=0;i<size;i++)
		{
			btree.insert(in.nextInt());
		}
		System.out.println("Find something here");
		boolean r=btree.find(in.nextInt());
		if(r){System.out.println("Found..Hurray");}
		else{
			System.out.println("It is not here :(");
		}
		r=btree.find(in.nextInt());
		if(r){System.out.println("Found..Hurray");}
		else{
			System.out.println("It is not here :(");
		}
		r=btree.find(in.nextInt());
		if(r){System.out.println("Found..Hurray");}
		else{
			System.out.println("It is not here :(");
		}
		btree.inOrder();
		btree.preOrder();
		btree.postOrder();
		
}
	
	
}
