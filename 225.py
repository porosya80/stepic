shapes = int(input())

def check_shapes(shapes):
    if 1 < shapes > 4:
        return "There is no such shape!"

    if shapes == 1:
        figure = "square"
    elif shapes == 2:
        figure = "circle"
    elif shapes == 3:
        figure = "triangle"
    elif shapes == 4:
        figure = "rhombus"




    return "You have chosen a " + figure

print(check_shapes(shapes))

# 1 – square, 2 – circle, 3 – triangle, 4 – rhombus