def inorder_dfs(tree, current_vertex):
	# Edge case: input tree is empty
	if current_vertex in tree:
		left_neighbour, right_neighbour = tree[current_vertex]
		if left_neighbour:
			inorder_dfs(tree, left_neighbour)
		print(current_vertex)
		if right_neighbour:
			inorder_dfs(tree, right_neighbour)

def dfs(tree, start):
	inorder_dfs(tree, start)

tree = {
    'B': ['D', 'E'],
    'A': ['B', 'C'],
    'C': ['F', 'G'],
    'D': [None, None],
    'E': [None, None],
    'F': [None, None],
    'G': [None, None]
}

#tree = {}

# Call in-order DFS starting from node 'A'
dfs(tree, 'A')

'''

		A
	  /   \
	 B     C
    / \   / \
   D   E F   G


|                 |			   |                 |			   |                 |			   |                 |		|                 |
|-----------------|			   |-----------------|			   |-----------------|			   |-----------------|		|-----------------|
| dfs(graph, 'D') |-> print: D | 	  pop(D)	 |			   | dfs(graph, 'E') |-> print: E  | 	  pop(E)	 |		|				  |
|-----------------|			   |-----------------|			   |-----------------|			   |-----------------| -> 	|-----------------|
| dfs(graph, 'B') |			   | dfs(graph, 'B') |-> print: B  | dfs(graph, 'B') |			   | dfs(graph, 'B') |		| 	   pop(B)	  |
|-----------------|			   |-----------------|			   |-----------------|			   |-----------------|		|-----------------| -> print: A
| dfs(graph, 'A') |			   | dfs(graph, 'A') |			   | dfs(graph, 'A') |			   | dfs(graph, 'A') |		| dfs(graph, 'A') |
-------------------			   -------------------			   -------------------			   -------------------		-------------------

|                 |			   |                 |			   |                 |			   |                 |				|                 |
|-----------------|			   |-----------------|			   |-----------------|			   |-----------------|				|-----------------|
| 				  |-> 		   | dfs(graph, 'F') |-> print: F  |      pop(F)	 |  		   | dfs(graph, 'G') |-> print: G	|	   pop(G)	  |
|-----------------|			   |-----------------|			   |-----------------|			   |-----------------|				|-----------------|
| dfs(graph, 'C') |			   | dfs(graph, 'C') |			   | dfs(graph, 'C') |-> print: C  | dfs(graph, 'C') |				| 	   pop(C)	  |
|-----------------|			   |-----------------|			   |-----------------|			   |-----------------|				|-----------------|
| dfs(graph, 'A') |			   | dfs(graph, 'A') |			   | dfs(graph, 'A') |			   | dfs(graph, 'A') |				| 	   pop(A)	  |
-------------------			   -------------------			   -------------------			   -------------------				-------------------

D, B, E, A, F, C, G

'''