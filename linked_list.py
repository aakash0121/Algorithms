class Node(object):
    
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def setData(self, data):
        self.data = data
        
    def getData(self):
        return self.data
    
    def setNext(self, next):
        self.next = next

    def getNext(self):
        return self.next
    
class LinkedList(object):

    def __init__(self):
        self.head = None

    def traverse_linked_list(self):
        if (self.head == None):
            print("linked list is empty")
            return

        temp = self.head
        while (temp != None):
            print(temp.data, end = ' ')
            temp = temp.next
        print("\n")
    
    def insert_at_start(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def insert_after_data(self, previousData, data):
        temp = self.head
        while (temp.data != previousData):
            temp = temp.next
            if temp == None:
                print("the data which you have entered is not in the linked list")
                break
        else:
            newNode = Node(data)
            newNode.next = temp.next
            temp.next = newNode
    
    def insert_at_end(self, data):
        if (self.head == None):
            self.insert_at_start(data)
        else:
            newNode = Node(data)
            temp = self.head
            
            while (temp.next != None):
                temp = temp.next
            
            temp.next = newNode
    
    def delete(self, data):
        current = self.head

        if (current.data == data):
            self.head = current.next
        else:
            current = self.head.next
            previous = self.head
            while (current.data != data):
                current = current.next
                previous = previous.next
                if (current == None):
                    print("data doesn't exist in the linked list")
                    break
            else:
                previous.next = current.next
    
    def search_data(self, data):
        if self.head == None:
            print("linked list is empty")
        else:
            temp = self.head
            
            while(temp.data != data):
                
                temp = temp.next
                if (temp == None):
                    print("Specified data does not exist in the linked list")
                    break
                
            else:
                print("Specified data is present")

if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert_at_end(3)
    linked_list.insert_at_start(1)
    linked_list.insert_after_data(1, 2)
    linked_list.traverse_linked_list()
    linked_list.search_data(2)
    linked_list.delete(2)
    linked_list.delete(3)
    linked_list.delete(1)
    linked_list.traverse_linked_list()