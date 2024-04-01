import math

def square(side):
    if isinstance(side, int):
        return side * side
    else:
        return math.ceil(side) * math.ceil(side)

side_length = 4.5 
area = square(side_length)
print("Площадь квадрата с длиной стороны", side_length, "равна", area)