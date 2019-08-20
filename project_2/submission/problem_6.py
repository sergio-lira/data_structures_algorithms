import random

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    def __contains__(self, item):
        if self.head is None:
            return False

        node = self.head
        while node:
            if node.value == item.value:
                return True
            node = node.next

        return False

def union(llist_1, llist_2):
    if llist_1 is None:
        return llist_2
    elif llist_2 is None:
        return llist_1

    union_set = LinkedList()
    node1 = llist_1.head
    while node1:
        if not node1 in union_set:
            union_set.append(node1.value)
        node1 = node1.next

    node2 = llist_2.head
    while node2:
        if not node2 in union_set:
            union_set.append(node2.value)
        node2 = node2.next

    return union_set



def intersection(llist_1, llist_2):
    if llist_1 is None:
        return llist_2
    elif llist_2 is None:
        return llist_1

    result_set = LinkedList()
    node1 = llist_1.head
    node2 = llist_2.head

    while node1:
        if node1 in llist_2 and not node1 in result_set:
            result_set.append(node1.value)
        node1 = node1.next

    return result_set


print("<<< Test Case 1 >>>")

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print ('Union:\n'+str(union(linked_list_1,linked_list_2)))
#Expect all elements without repated entries
print ('Intersection:\n'+str(intersection(linked_list_1,linked_list_2)))
#Expect 3 elements

print("\n<<< Test Case 2 >>>")

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print ('Union:\n'+str(union(linked_list_3,linked_list_4)))
#Expect all elements without repated entries
print ('Intersection:\n'+str(intersection(linked_list_3,linked_list_4)))
#Expect an empty set

print("<<< Test Case 3 >>>\n Larger randomized test case")
random.seed(5)
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [random.randint(0,1000) for _ in range(0, 100)]
element_2 = [random.randint(0,1000) for _ in range(0, 100)]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print ('Union:\n'+str(union(linked_list_5,linked_list_6)))
print ('Intersection:\n'+str(intersection(linked_list_5,linked_list_6)))

print("<<< Test Case 4 >>>\n One of the lists is empty")
random.seed(5)
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = []
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print ('Union:\n'+str(union(linked_list_5,linked_list_6)))
print ('Intersection:\n'+str(intersection(linked_list_5,linked_list_6)))

print("<<< Test Case 5 >>>\n Both lists are empty")
random.seed(5)
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print ('Union:\n'+str(union(linked_list_5,linked_list_6)))
print ('Intersection:\n'+str(intersection(linked_list_5,linked_list_6)))
