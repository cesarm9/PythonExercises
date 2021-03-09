minutes = int(input("Type the minutes: " ))
secondsinaminute = 60

def minutestoseconds(minutes, secondsinaminute):
    result = minutes*secondsinaminute
    return result

print(f'there are {minutestoseconds(minutes,secondsinaminute)} seconds in {minutes}')