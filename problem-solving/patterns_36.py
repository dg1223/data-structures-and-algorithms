# https://github.com/kunal-kushwaha/DSA-Bootcamp-Java/blob/main/assignments/09-patterns.md
'''
36. 4 4 4 4 4 4 4 
	  3 3 3 3 3 
	    2 2 2 
	      1 
	    2 2 2 
	  3 3 3 3 3 
	4 4 4 4 4 4 4
'''

def pattern36(n):
    pattern = ''
    matrix_size = 2*n-1
    edge_counter = 0
    for row in range(1, matrix_size+1):
        if row > n:
            col_counter -= 1
            edge_counter -= 1
            pattern += '  ' * (col_counter-1)
            for column in range(col_counter, matrix_size+1-(edge_counter-1)):
                # print(f"edge_counter = {edge_counter}")
                pattern += str(n-col_counter+1) + ' '
        else:
            col_counter = row
            pattern += '  ' * (col_counter-1)
            for column in range(col_counter, matrix_size+1-edge_counter):
                pattern += str(n-col_counter+1) + ' '
            edge_counter += 1
            
        pattern += '\n'        
        
    return pattern

print(pattern36(4))
