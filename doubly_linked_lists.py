class DoublyLinkedList(object):
	def __init__(self):
		self.head = None
		self.tail = None


	def Append(self,node):						#this adds node to end of list
		
		newnode = Node(node)
		if (self.head == None):					#means this is empty list, so this is the first node being added
			self.head = self.tail = newnode		#head, tail and node values are same for first node
			self.prev = None 					#there are no prev or next values yet, so set prev and next to None
			self.next = None
		else:									#this is not the first node, so there are already head and tail values		
			newnode.prev = self.tail 			#set current node value to new node									
			self.tail.next = newnode 			#set previous node's next link to new node
			
			self.tail = newnode 				#set new tail to current node
			self.next = None 					#set new node next link to none

  		return self
	
	def Insert(self,newnode,position,targetnode):	#this inserts node either before or after a target node
		
		current = self.head 						#start at head node
		while current != None:
			if current.value == targetnode:			#look for node matching target node
				if position == "before":			#insert a new node before a target node
					newnext = current				#get the current node (which is the target node)
					newprev = current.prev 			#get the current node's previous node
					newnode = Node(newnode,newprev,newnext)	#create new node, passing values for prev and next links
					current.prev.next = newnode 	#reset the previous node's next link to the new node
					current.prev = newnode 			#reset the current node's prev to the new node

				else:								#insert a new node after a target node
					newnext = current				#get the current node (which is the target node)
					newprev = current 				#get the current node, which will be the new node's prev
					newnext = current.next 			#get the current node's next, which will be the new node's next
					newnode = Node(newnode,newprev,newnext)	#create new node, passing values for prev and next links
					current.next.prev = newnode 	#reset current node's next node's prev to the new node
					current.next = newnode			#reset the current node's next to the new node
				
				return True
		  	current = current.next 					#get the next node
		print "**************OOPS, target value (",targetnode,") not found!************"
		return False


	def Del(self,node):
		current = self.head 						#start at the head node
		while current != None:
		 	if current.value == node:				#look for node matching node to delete
				current.prev.next = current.next 	#reset current node's previous node's next link to current node's next node
				current.next.prev = current.prev 	#reset current node's next node's prev link to current node's previous node
		 		return True
		  	current = current.next
		return False


	def PrintAll(self):
		current = self.head
		while current != None:
			print "Node:",current.value
			if current.prev != None:
				print "Node.prev:", current.prev.value
			else:
				print "Node.prev:", current.prev


			if current.next != None:
				print "Node.next:",current.next.value,"\n"
			else:
				print "Node.next:",current.next,"\n"
			
			current = current.next
		return True

	
	def PrintAll2(self):
		current = self.head
		print "Prev -- Node -- Next"
		while current != None:
			#print current.value
			if current.prev != None:
				print current.prev.value,"--",current.value,"--",
			else:
				print current.prev,"--",current.value,"--",

			if current.next != None:
				print current.next.value,"\n"
			else:
				print current.next,"\n"
			
			current = current.next
		return True
  


class Node(object):
	def __init__(self,node,prev=None,next=None):
		self.value = node
		self.next = next		 
		self.prev = prev		
		


#instantiate the list
dlList = DoublyLinkedList()
#dlList.NodeInfo()

#add values to list
dlList.Append(23)
# dlList.NodeInfo()


dlList.Append(25)
#dlList.NodeInfo()


dlList.Append(39)
#dlList.NodeInfo()


dlList.Append(47)
#dlList.NodeInfo()

print "\n****************Doubly linked list with values****************"
dlList.PrintAll()

print "\n*************************Delete node 39***********************"
dlList.Del(39)

dlList.PrintAll()

print "\n***********************Insert 99 before 39********************"
dlList.Insert(99,"before",39)
dlList.PrintAll()

print "\n************************Insert 88 after 25********************"
dlList.Insert(88,"after",25)
dlList.PrintAll()

print "\n*******************Print list with different format************"
dlList.PrintAll2()