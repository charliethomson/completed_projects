
class Node:
	def __init__(self, data=None, index=None):
		self.next = None
		self.last = None
		self.data = data
		self.index = index

	def __repr__(self):
		return f"Node object with index {self.index} holding data {self.data}"

	# all of these are just to compare the data the nodes hold rather than the nodes themselves
	def __gt__(self, other):
		return self.data > other.data

	def __lt__(self, other):
		return self.data < other.data

	def __ge__(self, other):
		return self.data >= other.data

	def __le__(self, other):
		return self.data <= other.data

	def __eq__(self, other):
		return self.data == other.data

	def __ne__(self, other):
		return self.data != other.data

	def __add__(self, other):
		return self.data + other.data

	def __sub__(self, other):
		return self.data - other.data

	def __mul__(self, other):
		return self.data * other.data

	def __div__(self, other):
		return self.data / other.data




class LinkedList:
	def __init__(self, *data):
		# dunders to make them unaccessable to the end user see PEP8 -> (https://www.python.org/dev/peps/pep-0008/#method-names-and-instance-variables)
		self.__head = Node()
		self.__tail = Node()
		self.__head.next = self.__tail
		self.__tail.last = self.__head
		
		for d in data:
			self.append(d) # if you pass any type of list, the append function breaks it up

	def __add__(self, other):
		# return a new linked list with the data from the first one before the data from the second one
		# x = [1, 2, 3]
		# y = [4, 5, 6] 
		# z = x + y
		# z = [1, 2, 3, 4, 5, 6]
		new = LinkedList()
		new.append(self)
		new.append(other)
		return new

	def __contains__(self, data):
		# returns true if "data" is in the list, else, false (<value> in <LinkedList>)
		current = self.__head.next
		while current is not self.__tail: # walk the list
			if current.data == data: 	# if it sees the data, it'll return true and exit
				return True
			current = current.next		

		return False # else it'll return false

	def __len__(self):
		# returns the length of the list (len(<LinkedList>))
		current = self.__head.next
		count = 0

		while current is not self.__tail: # walk the list
			count += 1					# count the nodes
			current = current.next
		return count 					# return the count

	def __iter__(self):
		# makes the list iterable (for <value> in <LinkedList>: do stuff)
		current = self.__head.next

		while current is not self.__tail: # walk the list
			yield current.data			# yielding each node's data
			current = current.next		# before moving to the next node

	def __getitem__(self, input_):
		# allows for indexing <LinkedList>[1]; returns the first index of the list, 
						    # <LinkedList>[1:11:2]; returns every other index of the list between the first and eleventh indices)
		if isinstance(input_, slice): 	# if the data it recieves is a slice (ex. LinkedList[0:5:2])
			current = self.__head.next
			start = input_.start if input_.start else 0		  # these are ternary operators
			stop  = input_.stop if input_.stop else len(self) # they're used here to check if the values were given
			step  = input_.step if input_.step else 1		  # (the slice object has start, stop, and step values that are None by default)
															  # so we have to check if they exist and if they don't, give them my default values
			return_list = LinkedList()	
			count, counting = 0, False
			while current is not self.__tail: # walk the list
				if current.index == start: 	# if it's at start, start counting
					counting = True
				if current.index == stop: 	# if it's at stop, exit the loop
					break
				if counting:				# if it's counting, count
					count += 1
				if count % step == 0:		# if we've walked "step" steps, add the data to the list 
					return_list.append(current.data)
				current = current.next
			return return_list
		elif isinstance(input_, int):  # if the data it recieves is an int (ex. LinkedList[4])
			current = self.__head.next
			index = input_
			while current is not self.__tail: # walk the list
				if current.index == index:	# if we find the index, return the data there
					return current.data
				current = current.next

			raise IndexError(f"index {index} is out of range")

		return None 						

	def __delitem__(self, input_):
		# allows for index deletion (del <LinkedList>[1] deletes the first index,
								   # del <LinkedList>[1:11:2] deletes every other index between the first and eleventh index)
		if isinstance(input_, slice): # if it's a slice
			start = input_.start if input_.start else 0
			stop  = input_.stop  if input_.stop  else len(self) - 1
			step  = input_.step  if input_.step  else 1

			count, counting = 0, False
			
			current = self.__head.next
			while current is not self.__tail:
				if current.index == start: # start counting at start
					counting = True
				if current.index == stop:  # exit the loop at stop
					break
				if counting: 
					count += 1 # increment the count if it's started
					if count % step == 0: 
						self.__delitem__(current.index) # if we've gone "step" steps, remove that data
				current = current.next
			
			index = 0
			
			current = self.__head.next
			while current is not self.__tail: # fix the indices
				current.index = index
				index += 1
				current = current.next
		
		elif isinstance(input_, int): # if it's an integer (index)
			
			index = input_

			current = self.__head.next
			while current is not self.__tail: # walk the list
				if current.index == index:  # until it's at the right index
					current.last.next = current.next # from: last -> current -> next
					current.next.last = current.last # to  : last -> next, current
					return current.data		# skip, return the data
				current = current.next 

	def __setitem__(self, index, data):
		# sets an item at the given index's data to the given data (<LinkedList>[index] = data)
		current = self.__head.next
		while current is not self.__tail: # walk the list
			if current.index == index: 	# until we're at the right index,
				current.data = data		# change the data, and exit
				return None					
			current = current.next

		raise IndexError(f"index {index} out of range")

	def __repr__(self):
		# gets called when the print() function is used
		# iterate over the list, converting each item into a string, 
		# then use the str.join() function to join them in an f-string with [] around it
		return f"[{', '.join([str(item) for item in self])}]" 

	def help(self):
		# display the help docs, shows functions and args 
		print("\nall_indices(data): return a linked list of the indices of all instances of 'data'\n")
		print("\nappend(data): add 'data' to the end of the linked list\n")
		print("\nclear(): remove all data from the linked list\n")
		print("\ncount(data): return the number of instances of 'data' in the linked list\n")
		print("\nextend(<LinkedList> other): adds the data from 'other' to the end of the list\n")
		print("\nhelp(): display this help page\n")
		print("\nindex(data): return the first index of 'data'\n")
		print("\ninsert(index, data): insert 'data' at index 'index'\n")
		print("\npop(index=None): remove the data at index 'index'; if 'index' is None, removes the last item in the linked list\n")
		print("\nremove(data): remove the first instance of 'data'\n")
		print("\nremove_all(data): remove all instances of 'data'\n")
		print("\nreplace(old, new): replace all instances of 'old' with 'new'\n")
		print("\nreverse(): reverses the list (INPLACE)\n")
		print("\nsort(): (bubble) sort the list (INPLACE) \n")

	def append(self, *args):
		########################################
		## add a value to the end of the list ##
		########################################
		for data in args:
			if type(data) is list or   \
			   type(data) is tuple or  \
			   type(data) is LinkedList: # if it's any kind of iterable, break up the iterable and add the items to the list
				[self.append(item) for item in data]; continue
			
			new_node = Node(data, 0)

			current = self.__head
			while current.next is not self.__tail: # walk the list
				new_node.index += 1 			 # increasing the new node's index
				current = current.next

			current.next = new_node	# put the new node at the end of the list
			new_node.last = current
			new_node.next = self.__tail
			self.__tail.last = new_node


	def remove(self, data):
		##########################################################
		## remove the first instance of the value from the list ##
		##########################################################
		current = self.__head

		while current.data != data: # walk the list, looking for the data
			current = current.next
			if current is self.__tail: raise ValueError(f"{data} not found") # if it gets to the end, raise an error

			# if it gets here, current has the data we were looking for
		current.last.next = current.next  # skip the item
		current.next.last = current.last  # l -> c -> n => l -> n; c
		current = current.next
		current.index -= 1

		while current.next is not self.__tail: # walk the list
			current = current.next
			current.index -= 1				 # fixing the indices



	def remove_all(self, data):
		####################################################
		## remove all instances of the data from the list ##
		####################################################
		current = self.__head.next
		removed = 0	# used for fixing the indices

		while current is not self.__tail: # walk the list
			if current.data == data:	# if we find the data
				removed += 1 			# add one to the removed
				current.last.next = current.next # remove the item from the list
				current.next.last = current.last
			current.index -= removed	# fix the indices
			current = current.next

		# if it didn't find any instances of the data, raise an error
		if removed == 0: raise ValueError(f"0 instances of {data} found") 

	def pop(self, index=None):
		####################################################
		## remove the node at index "index" from the list ##
		####################################################
		current = self.__head
		found = False
		ret = None
 
		while current.next is not self.__tail: # walk the list
			if index:						 # if an index was given
				if current.index == index:	 # if we found the index
					found = True 			 # used to fix the indices
					ret = current.data
					current.last.next = current.next # skip the found node
					current.next.last = current.last
			if found:
				current.index -= 1 # fix the indices

			current = current.next

		if index is None: # if there's no given index, remove the last index
			current.last.next = self.__tail
			self.__tail.last = current.last
			ret = current.data

		return ret # return the item that was removed


	def extend(self, other):
		################################################
		## add the values of other to the end of self ##
		################################################
		current = self.__head
		other_current = other.__head.next

		index = 0

		if self.__head.next is not self.__tail: # if the list is not empty
			while current.next is not self.__tail: # walk the list (get to the end of the list)
				current = current.next

			index = current.index + 1 

		else: # if the list is empty
			self.__head.next = other_current # make the head's next the other one's head's next

		while other_current is not other.__tail: # walk the other list
			temp = Node(other_current.data, index) # make new nodes with the correct data and index
			index += 1						   # increment the index

			current.next = temp				   # add the new node to the end of the list
			temp.last = current

			other_current = other_current.next # walk both lists
			current = current.next

		current.next = self.__tail # close out the list 
		self.__tail.last = current


	def insert(self, index, data):
		#####################################################
		## insert a new node with data data at index index ##
		#####################################################
		current = self.__head
		new_node = Node(data, index)
		found = False

		while current is not self.__tail: 	 # walk the list
			if current.index == index:		 # when we find the right index
				current.last.next = new_node # add the data to the list at that index
				new_node.last = current.last
				new_node.next = current
				current.last = new_node
				found = True 				 # say we found it

			if found:
				# if we found it, fix all following indices
				current.index += 1			

			current = current.next

		if not found:
			# raise an error if the index is never found
			raise IndexError(f"Index out of range")

	def clear(self):
		#####################
		## clears the list ##
		#####################
		self.__head.next = self.__tail # the head points to the tail,
		self.__tail.last = self.__head # the tail points to the head

	def count(self, data):
		###########################################################
		## counts how many instances of the data are in the list ##
		###########################################################
		count = 0
		current = self.__head.next

		while current is not self.__tail: # walk the list
			if current.data == data:	# if the data is what we're counting
				count += 1				# increment the counter
			current = current.next

		return count


	def index(self, data):
		#######################################################
		## gets the index of the first instance of data data ##
		#######################################################
		current = self.__head

		while current.data != data: # walk the list, looking for the data
			current = current.next
			if current is self.__tail: # if we get to the tail, raise an error
				raise ValueError(f"{data} not found")

		# if we get here, we found it, return the index we found
		return current.index

	def all_indices(self, data):
		#########################################################################
		## gets a list of all indices of all instances of the data in the list ##
		#########################################################################
		current = self.__head
		indices = LinkedList() # a list to hold the indices we found

		while current is not self.__tail: # walk the list
			if current.data == data:	# if we found the data
				indices.append(current.index) # add the index to the list
			current = current.next

		return indices

	def sort(self):
		############################
		## (bubble) sort the list ##
		############################
		def swap(current): # utility function, takes a Node current and swaps it and it's last Node
			last = current.last 
			# ll -> l -> c -> n
			# ll -> c -> l -> n
			current.next.last = last # l  <- n
			last.next = current.next # l  -> n
			current.next = last		 # c  -> l
			current.last = last.last # ll <- c
			last.last.next = current # ll -> c
			last.last = current 	 # c  <- l
			current.index -= 1		 # move the index back one
			last.index += 1			 # move the index forward one

		completed = False
		while not completed:
			count = 0
			current = self.__head.next 
			while current.next is not self.__tail: # walk the list
				current = current.next
				if current.last > current: 
					swap(current) # swap them if the current is smaller than the last
					count += 1	  # increase the count if swapped

			completed = (count == 0) # if the count is 0, no swaps were done, exit the loop

	def reverse(self):
		######################
		## reverse the list ##
		######################
		new = LinkedList() # new list
		current = self.__tail.last

		while current is not self.__head: # walk the list backwards
			new.append(current.data)    # add each item to the new list 
			current = current.last		

		self.clear() 
		self.extend(new) # make the current list the new list (extend to an empty list will copy the contents)

	def replace(self, old, new):
		###########################################
		## replace all instances of old with new ##
		###########################################
		current = self.__head.next

		while current is not self.__tail: # walk the list
			if current.data == old:		# if we find the old data, change the data to the new data
				current.data = new

			current = current.next
