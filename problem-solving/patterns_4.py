# https://github.com/kunal-kushwaha/DSA-Bootcamp-Java/blob/main/assignments/09-patterns.md
'''
4.  1
    1 2
    1 2 3
    1 2 3 4
    1 2 3 4 5
'''

def pattern4(n):
    pattern = ''
    col_counter = 1
    for row in range(n):
        for column in range(col_counter):        
            pattern += str(column+1) + ' '
        pattern = pattern.lstrip()
        pattern += '\n'
        col_counter += 1
    return pattern

print(pattern4(5))
