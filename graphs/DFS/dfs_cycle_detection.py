'''
O(V+E) time, O(V) space
'''

visited = set()

found_cycle = False

def dfs(graph, source, found_cycle, parent_array=None):

    #print(source)

    '''
    We can't initialize parent array globally as an empty 
    dictionary because we are mapping it against every key 
    in the graph and checking them in the for loop below.
    '''
    if not parent_array:
        parent_array = {key: -1 for key in graph}

    visited.add(source)

    for child in graph[source]:
        #breakpoint()
        if child in visited and parent_array[source] != child:
            found_cycle = True
            break

        if child not in visited:
            parent_array[child] = source
            dfs(graph, child, found_cycle, parent_array)

    return found_cycle

'''
            A
        /	  	\
       B     	 C
     / 	 \     /
    D     E - F
'''

graph_1 = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

'''
The for loop takes care disconnected components
'''
for vertex in graph_1:
    if vertex not in visited:
        cycle_found = dfs(graph_1, vertex, found_cycle)

if cycle_found:
    print("Cycle found in graph 1")
else:
    print("Cycle not found in graph 1")

'''
         0	    3
        /	 / 	   \
       1    4 	    6
      /	     \     /
     2          5
'''

graph_2 = {
     '0': ['1'],
     '1': ['0', '2'],
     '2': ['1'],
     '3': ['4', '6'],
     '4': ['3', '5'],
     '5': ['4', '6'],
     '6': ['3', '5']
}

'''
The for loop takes care disconnected components
'''
for vertex in graph_2:
    if vertex not in visited:
        cycle_found = dfs(graph_2, vertex, found_cycle)

if cycle_found:
    print("Cycle found in graph 2")
else:
    print("Cycle not found in graph 2")

'''
Directed graph

         0	    3
        /	 / 	   \
       .	.		.
       1    4 	    6
      /	     \     /
     .		  .   .
     2          5
'''

graph_3 = {
     '0': ['1'],
     '1': ['2'],
     '2': [],
     '3': ['4'],
     '4': ['5'],
     '5': ['6'],
     '6': ['3']
}

for vertex in graph_3:
    if vertex not in visited:
        cycle_found = dfs(graph_3, vertex, found_cycle)

if cycle_found:
    print("Cycle found in graph 3")
else:
    print("Cycle not found in graph 3")
