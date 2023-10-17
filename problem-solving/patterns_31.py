# https://github.com/kunal-kushwaha/DSA-Bootcamp-Java/blob/main/assignments/09-patterns.md
'''
31.      4 4 4 4 4 4 4
         4 3 3 3 3 3 4
         4 3 2 2 2 3 4
         4 3 2 1 2 3 4
         4 3 2 2 2 3 4
         4 3 3 3 3 3 4
         4 4 4 4 4 4 4
'''

def pattern31(n):
    pattern = ''
    original_n = n
    # we get 81 items from the following n -> 9^2
    # n = 2*n
    # we need 49 items for the solution, -> 7^2
    n = 2*n-2
    for row in range(n+1):
        for col in range(n+1):
            # print this pattern to understand the logic first
            # atEveryIndex = min(min(row, col), min(n-row, n-col))

            # print this pattern to get the inverted solution to above 
            atEveryIndex = original_n - min(min(row, col), min(n-row, n-col))

            # This is the solution
            atEveryIndex = original_n - min(min(row, col), min(n-row, n-col))

            pattern += str(atEveryIndex) + ' '

        pattern += '\n'
    return pattern

print(pattern31(4))
