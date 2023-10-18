# https://github.com/kunal-kushwaha/DSA-Bootcamp-Java/blob/main/assignments/09-patterns.md
'''
17.      1
        212
       32123
      4321234
       32123
        212
         1
'''

def pattern17(n):
    pattern = ''
    num_rows = 2*n-1    
    for row in range(1, num_rows+1):
        if row > n:
            col_counter -= 1
        else:
            col_counter = row

        for spaces in range(n-col_counter, 0, -1):
            pattern += ' '
        for column in range(col_counter, 0, -1):
            pattern += str(column)
        for column in range(2, col_counter+1):
            pattern += str(column)
        pattern += '\n'
    return pattern

print(pattern17(4))
