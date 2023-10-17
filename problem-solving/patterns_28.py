# https://github.com/kunal-kushwaha/DSA-Bootcamp-Java/blob/main/assignments/09-patterns.md

'''
28.      *
        * *
       * * *
      * * * *
     * * * * *
      * * * *
       * * *
        * *
         *
'''

# number of rows = 2n-1
def pattern28(n):
    pattern = ''    
    num_rows = 2*n-1
    col_counter = 1
    num_spaces_decremented = 2
    for row in range(num_rows):
        # impossible case handling
        if col_counter == 0:
            print("This cannot happen. Revisit your logic. Exiting program...")
            break
        # put pen on paper to understand the concept
        num_spaces = n - row        
        if col_counter == 1 and num_spaces > 0:            
            pattern += (' ' * num_spaces) + ('*' * col_counter) + (' ' * num_spaces)
        elif col_counter != 1 and num_spaces > 0:
            pattern += (' ' * num_spaces) + ('* ' * col_counter) + (' ' * (num_spaces-1))
        elif col_counter != 1 and num_spaces <= 0:
            pattern += (' ' * num_spaces_decremented) + ('* ' * col_counter) + (' ' * (num_spaces_decremented-1))
            num_spaces_decremented += 1
        else:
            pattern += (' ' * num_spaces_decremented) + ('*' * col_counter) + (' ' * num_spaces_decremented)
        
        pattern += '\n'
        
        if row >= n-1:
            col_counter -= 1
        else:
            col_counter += 1
    return pattern

print(pattern28(5))
