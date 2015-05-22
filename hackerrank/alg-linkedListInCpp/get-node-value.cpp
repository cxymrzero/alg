#include <iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;
struct Node
{
    int data;
    Node *next;
};
/*
  Get Nth element from the end in a linked list of integers
  Number of elements in the list will always be greater than N.
  Node is defined as 
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
int GetNode(Node *head, int positionFromTail)
{
    int len = 0, positionFromHead, cnt = 0;
    Node* tmp = head;
    while (tmp != NULL) {
        tmp = tmp->next;
        len++;
    }
    cnt = positionFromHead = len - positionFromTail;
    tmp = head;
    for (; cnt > 1; cnt--) {
        tmp = tmp->next;
    }
    return tmp->data;
}

void Print(Node *head)
{
    bool ok = false;
    while(head != NULL)
    {
        if(ok)cout<<" ";
        else ok = true;
        cout<<head->data;
        head = head->next;
    }
}
Node* Insert(Node *head,int x)
{
   Node *temp = new Node();
   temp->data = x;
   temp->next = NULL;
   if(head == NULL) 
   {
       return temp;
   }
   Node *temp1;
   for(temp1 = head;temp1->next!=NULL;temp1= temp1->next);
   temp1->next = temp;return head;
}
int main()
{
    int t;
    cin>>t;
    while(t-- >0)
    {
        Node *A = NULL;
        int m;cin>>m;
        while(m--){
            int x; cin>>x;
            A = Insert(A,x);}
        int n;cin>>n;
        cout<<GetNode(A,n)<<"\n";
    }
}