class linkedlistnode:
  def __init__(self,value,nextnode = None):
    self.value = value
    self.nextnode = nextnode

class linkedlist:
  def __init__(self,head = None):
    self.head = head

  def insertnew(self,value):
    node = linkedlistnode(value)
    if self.head is None:
      self.head = node
      return
    currentnode = self.head
    while True:
      if currentnode.nextnode is None:
        currentnode.nextnode = node
        break
      currentnode = currentnode.nextnode
      print("None")


  def printl(self):
    currentnode = self.head
    while currentnode is not None:
      print(currentnode.value,"->",end = "")
      currentnode = currentnode.nextnode
    print ("None")


ll = linkedlist()
ll.insertnew(5)
ll.insertnew(8)
ll.insertnew(9)
ll.printl()
