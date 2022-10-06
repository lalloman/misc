class Node:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None

class SLinkedList:
   def __init__(self):
      self.headval = None

list1 = SLinkedList()
list1.headval = Node("first item")
e2 = Node("second item")
e3 = Node("third item")

list1.headval.nextval = e2

e2.nextval = e3