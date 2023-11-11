# Find log base 2 of 32-bit integer
def log_base_2(number):
    count = 0
    while number > 1:
        print(f"{number = }")
        number >>= 1
        count += 1
    return count

print(log_base_2(64))