# https://github.com/kunal-kushwaha/DSA-Bootcamp-Java/blob/main/assignments/09-patterns.md
'''
5.  *
    **
    ***
    ****
    *****
    ****
    ***
    **
    *
'''

# number of rows = 2n-1
def pattern5(n):
    pattern = ''    
    num_rows = 2*n-1
    col_counter = 1
    for row in range(num_rows):        
        for column in range(col_counter):        
            pattern += '* '
        pattern = pattern.rstrip()        
        pattern += '\n'
        
        # put pen on paper to understand this
        if row >= n-1:
            col_counter -= 1
        else:
            col_counter += 1
    return pattern

print(pattern5(5))
