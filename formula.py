signWidthInches = 11
signHeightInches = 5.75


def roundConvertToPoints(dimension):

    # Round inches to nearest half inch
    if dimension % 1 >= .5:
        dimension = int(dimension) + 1
    else:
        dimension = int(dimension)

    # Covnvert to points
    dimension = dimension * 72

    return dimension


horizontalAxis = roundConvertToPoints(signWidthInches)
verticalAxis = roundConvertToPoints(signHeightInches)


def findShortestAxis():
    if horizontalAxis < verticalAxis:
        shortestAxis = horizontalAxis
    else:
        shortestAxis = verticalAxis
    return shortestAxis


A = findShortestAxis() * .15
B = verticalAxis * .15



size(horizontalAxis, verticalAxis)
