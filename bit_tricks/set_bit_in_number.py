# num = number, pos = position at which we want to set the bit
def set (num, pos):
    # First step = Shift '1'
    # Second step = Bitwise OR
    num |= (1 << pos)
    print(num)

num, pos = 4, 1
set(num, pos)