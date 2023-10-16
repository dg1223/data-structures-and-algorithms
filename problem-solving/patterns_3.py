# https://github.com/kunal-kushwaha/DSA-Bootcamp-Java/blob/main/assignments/09-patterns.md

def pattern3(n):
    pattern = ''
    for row in range(n):
        for column in range(n-row):
            pattern += '*'
        pattern += '\n'
    return pattern

print(pattern3(5))
