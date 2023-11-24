class DFS:
	def __init__(self, value):
		self.value = value
		self.children = []

	def dfs(self, start_node, target):
		path = [start_node]

		# No need to proceed if we already found a match
		if start_node.value == target:
			print(f"Visiting {start_node.value}")
			return path
		
		'''
		We can either store the start node and path as a 
		tuple and pop both at the same time using double 
		assignment or we can store them as individual 
		items in a list and pop them separately using 
		their indices.
		We also have to append child and path accordingly.
		'''
		frontier = [(start_node, path)]
		#frontier = [start_node, path]

		while frontier:
			current_node, path = frontier.pop()
			#path = frontier.pop()
			#current_node = frontier.pop()			
			print(f"Visiting : {current_node.value}")
			if current_node.value == target:
				return path
			for child in current_node.children:				
				frontier.append((child, path + [child]))
				#frontier.append(child)
				#frontier.append(path + [child])

		return None

root = DFS('A')
two = DFS("B")
three = DFS("C")
root.children = [two, three]
four = DFS("D")
five = DFS("E")
six = DFS("F")
seven = DFS("G")
two.children = [five, four]
three.children = [seven, six]

start = root
target = 'F'
path = root.dfs(start, target)

if path:
	print(f"Path found from {start.value} to {target}")

	string = " -> ".join(node.value for node in path)

	print(string)
else:
	print(f"No path found from {start.value} to {target}")


'''

		A
	  /   \
	 B     C
    / \   / \
   D   E F   G

Find path from A -> F

|                 |	   |                 |			   |                   |	 |                   |					|                     |
|-----------------|	   |-----------------|			   |-------------------|	 |-------------------|					|---------------------|
| 				  |->  | 	  	 		 |			   | 				   |-> 	 | 	  			  	 |					|				      |
|-----------------|	   |-----------------|			   |-------------------|	 |-------------------| -> print: C 		| for loop:		      |
| 				  |	   | 	 pop(F)		 |-> print: A  | for loop:		   |	 | 	     pop(F)	  	 |	 path: [A, C]	| F = [(B, [A, B]),   |
|-----------------|	   |				 |   path: [A] | F = [(B, [A, B]), |	 |				  	 |					|     (G, [A, C, G]), | -> print: A
| F = [(A, [A])]  |	   | 	 F = [] 	 |			   |     (C, [A, C])]  |	 | F = [(B, [A, B])] |					|     (F, [A, C, F])] |
-------------------	   -------------------			   ---------------------	 ---------------------					-----------------------

|                 	  |			   		 |					|
|---------------------|			   		 |					|
| 				  	  |-> print F  		 |					|
|       pop(F)		  |	path: [A, C, F]	 | return [A, C, F]	|
|				  	  |			   		 |					|
| F = [(B, [A, B]),   |			   		 |					|
|     (G, [A, C, G]), |			   		 |					|
-----------------------			   		 --------------------

A, C, F

'''