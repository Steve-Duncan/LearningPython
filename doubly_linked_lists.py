class DoublyLinkedList(object):
	def __init__(self):
		self.head = None
		self.tail = None


	def Add(self,node):
		
		if (self.head == None):		#means this is empty list
			self.head = node 		#set current head to first value provided
			self.tail = self.head 	#set current tail to value of head, since this is the first (only) record
			self.prev = None 		#set prev and next to None
			self.next = None
		else:
			self.next = None		#for subsequent records added, set next to None
			self.prev = self.tail 	#set prev value to the previous tail
			self.tail = node 		#set new tail value to new record
  
	
	def NodeInfo(self):
		if self.head:				#if this is not an empty list, print values
			print "Head:",self.head
			print "Tail:",self.tail
			print "Prev:",self.prev
			print "Next:",self.next,"\n"

class Node(object):
	def __init__(self,value):
		self.value = value
		self.next = None		#had to set these values to None in Add method of DoublyLinkedList; 
		self.prev = None		# why can't they be set to None here?
		



dlList = DoublyLinkedList()
#dlList.NodeInfo()
dlList.Add(23)
dlList.NodeInfo()

dlList.Add(39)
dlList.NodeInfo()

dlList.Add(47)
dlList.NodeInfo()

dlList.Add(13)
dlList.NodeInfo()



