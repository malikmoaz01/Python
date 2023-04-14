#include <iostream>
using namespace std;

class Node {
public:
    int data;
    Node* prev;
    Node* next;
};

class DoublyLinkedList {
private:
    Node* head;

public:
    DoublyLinkedList() {
        head = NULL;
    }

    void insertEnd(int data) {
        Node* newNode = new Node();
        newNode->data = data;
        newNode->prev = NULL;
        newNode->next = NULL;

        if (head == NULL) {
            head = newNode;
        }
        else {
            Node* currNode = head;
            while (currNode->next != NULL) {
                currNode = currNode->next;
            }
            currNode->next = newNode;
            newNode->prev = currNode;
        }
    }

    void insertMiddle(int data, int position) {
        Node* newNode = new Node();
        newNode->data = data;
        newNode->prev = NULL;
        newNode->next = NULL;

        if (head == NULL) {
            head = newNode;
        }
        else {
            Node* currNode = head;
            int count = 1;
            while (currNode != NULL && count != position) {
                currNode = currNode->next;
                count++;
            }
            if (currNode == NULL) {
                cout << "Invalid position" << endl;
                return;
            }
            newNode->next = currNode->next;
            currNode->next = newNode;
            newNode->prev = currNode;
            if (newNode->next != NULL) {
                newNode->next->prev = newNode;
            }
        }
    }

    void display() {
        Node* currNode = head;
        while (currNode != NULL) {
            cout << currNode->data << " ";
            currNode = currNode->next;
        }
        cout << endl;
    }
};

int main() {
    DoublyLinkedList dll;
    dll.insertEnd(10);
    dll.insertEnd(20);
    dll.insertEnd(30);
    dll.insertMiddle(15, 2);
    dll.display();
    return 0;
}
