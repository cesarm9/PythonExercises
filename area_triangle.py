base = int(input("Input your triangle base: "))
height = int(input("Input your triangle height: "))


def trianglearea(base,height):
    area = base*height / 2
    return area

print(f'the area of your triangle is: {trianglearea(base,height)}')



