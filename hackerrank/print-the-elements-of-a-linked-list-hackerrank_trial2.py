def printLinkedList(head):
    
    # if head == Null:
    #     return 
        
    LocalNode= head
    
    while LocalNode:
        print(LocalNode.data)
        
        LocalNode= LocalNode.next