class Node
{
	int val;
	Node next;
	public Node(int val)
	{
		this.val=val;
		this.next=null;
	}
};
public class LinkedList
{
	Node head;
	
	public LinkedList(int val)
	{
		if(this.head==null){this.head=new Node(val);}
		
	}
	public void insertHead(int val)
	{
		Node node=new Node(val);
		Node temp=this.head;
		this.head=node;
		node.next=temp;
	}
	public void appendHead(int val)
	{
		Node node=new Node(val);
		Node temp=this.head;
		while(temp.next!=null){temp=temp.next;}
		temp.next=node;
		
	}
	public void insertAfter(int val,int after )
	{
		Node node=new Node(val);
		Node temp=this.head;
		while(temp.val!=after){temp=temp.next;}
		if(temp.next==null){System.out.println("The node is not found");}
		else{
			node.next=temp.next;
			temp.next=node;
		}
	}
	public void insertBefore(int val,int before )	
	{
		Node node=new Node(val);
		Node temp=this.head;
		while(temp.val!=before){temp=temp.next;}
		if(temp.next==null){System.out.println("The node is not found");}
		else{
			node.next=temp.next;
			temp=node;
		}
	}
	public Node delete(int val)
	{
		Node node=new Node(val);
		Node temp=this.head;
		while(temp.val!=val){temp=temp.next;}
		if(temp.next==null){System.out.println("value not found");return null;}
		else{temp.next=node.next;
		node.next=null;
		return node;
		}
		
		
	}
	
	public static void main(String[] args){
		
		LinkedList list=new LinkedList(10);
		list.insertHead(15);
		list.insertHead(16);
		list.appendHead(11);
		list.appendHead(12);
		list.insertAfter(100, 15);
		list.insertBefore(200, 15);
		Node temp=list.head;
		while(temp!=null){
		System.out.println(temp.val);
		temp=temp.next;
		}
	}
	
	
}
