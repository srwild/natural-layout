signWidthInches = 11
signHeightInches = 5.75


def convertToPoints(dimension):
    dimension = dimension * 72
    return dimension


horizontalAxis = convertToPoints(signWidthInches)
verticalAxis = convertToPoints(signHeightInches)


def findShortestAxis():
    if horizontalAxis < verticalAxis:
        shortestAxis = horizontalAxis
    else:
        shortestAxis = verticalAxis
    return shortestAxis


A = findShortestAxis() * .15
B = verticalAxis * .15


opticalCenter = horizontalAxis / 2, verticalAxis * .54

def drawopticalCenter():
    circleSize = 10
    circleSizeHalf = circleSize / 2

    with savedState():
        fill(1)
        cmykStroke(1, 0, 0, 0)
        strokeWidth(1)
        translate(opticalCenter[0] - circleSize / 2, opticalCenter[1] - circleSize / 2)
        oval(0, 0, circleSize, circleSize)
        line((-circleSizeHalf, circleSizeHalf), (circleSize + circleSizeHalf, circleSizeHalf))
        line((circleSizeHalf, circleSize + circleSizeHalf), (circleSizeHalf, -circleSizeHalf))




size(horizontalAxis, verticalAxis)

drawopticalCenter()

# saveImage("sheet.pdf")
