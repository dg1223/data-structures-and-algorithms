def add_two_to_target(items, target):
    # dictionary1 = {number: count}
    # find() -> first index of number and return
    if not items:
        return None
        print("Input is empty")
    head = 0
    tail = len(items) - 1
    FOUND = False
    while head < tail:
        result = items[head] + items[tail]
        if result == target:
            FOUND = True
            break
        else:
            if result > target:
                tail -= 1
            else:
                head += 1
        
    if FOUND:
        return items[head], items[tail]
    else:
        return None

items = [1, 2, 3, 4, 5]
indices = add_two_to_target(items, 7)
if indices:
    #print(f"{indices[0]}, {indices[1]}")
    print(indices)
else:
    print("No two indices match the target, sorry !!!")
