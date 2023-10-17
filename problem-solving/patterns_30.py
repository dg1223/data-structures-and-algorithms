# https://github.com/kunal-kushwaha/DSA-Bootcamp-Java/blob/main/assignments/09-patterns.md
'''
30.         1
          2 1 2
        3 2 1 2 3
      4 3 2 1 2 3 4
    5 4 3 2 1 2 3 4 5
'''

def pattern30(n):
    pattern = ''
    for row in range(1, n+1):
        # two spaces = 1 unit of space
        one_unit_space = '  '
        for spaces in range(n-row, 0, -1):
            pattern += one_unit_space
        for column in range(row, 0, -1):
            pattern += str(column) + " "
        for column in range(2, row+1):
            pattern += str(column) + " "
        pattern += '\n'
    return pattern

print(pattern30(5))
