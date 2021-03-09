minutes = int(input("Type the minutes: " ))
secondsinaminute = 60

def minutestoseconds(minutes, secondsinaminute):
    result = minutes*secondsinaminute
    return result

print("There are")

print(minutestoseconds(minutes,secondsinaminute))
print("seconds")
print("in")
print(minutes)
print("minutes")

print("There are:" minutestoseconds(minutes,secondsinaminute) "seconds")