#include <iostream>

using namespace std;
struct Node{
    int data;
    Node* link;
};
Node* top;
int maxsize=5;
int a=0;

void push(int data){

    Node* temp = new Node();
    if (a>maxsize)
    {
        cout << "\nStack is Full"<<endl;
        exit(1);
    }
    else{
        a++;
        temp->data = data;
        temp->link = top;
        top = temp;

    }

}
bool isEmpty(){
    if(top==NULL)
        return true;
    else
        return false;

}

void pop(){
    Node*temp;
    if(top==NULL){
        cout << "\nStack Underflow" << endl;
        exit(1);
    }
    else{
        temp=top;
        top=temp->link;
        free(temp);
    }
}
int Top(){
    if (!isEmpty())
        return top->data;
    else
        exit(1);
}

void print(){
    Node*temp;
    if(top==NULL){
        cout << "\nStack Underflow";
        exit(1);
    }else{
        temp=top;
        while(temp!=NULL){
            cout<<temp->data<<"-> ";
            temp=temp->link;
        }

    }

}
int main()
{
    push(1);
    push(2);
    push(3);
    push(4);
    push(5);

    print();

    cout << "\nTop element is " << Top() << endl;

    pop();
    pop();

    print();

    cout << "\nTop element is " << Top() << endl;

    cout<< "New stack is: "<< isEmpty()<<endl;

    return 0;
}