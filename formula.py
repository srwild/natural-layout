signWidthInches = 3
signHeightInches = 7.5


def convertToPoints(dimension):
    dimension = dimension * 72
    return dimension


signWidth = convertToPoints(signWidthInches)
signHeight = convertToPoints(signHeightInches)



opticalCenter = signWidth / 2, signHeight * .54

verticalAxis = signHeight
horizontalAxis = signWidth

def findShortestAxis():
    if verticalAxis < horizontalAxis:
        shortestAxis = verticalAxis
    else:
        shortestAxis = horizontalAxis
    return shortestAxis


A = findShortestAxis() * .15
B = horizontalAxis * .17


def drawopticalCenter():
    circleSize = 10
    circleSizeHalf = circleSize / 2

    with savedState():
        fill()
        cmykStroke(1, 0, 0, 0)
        strokeWidth(1)
        translate(opticalCenter[0] - circleSize / 2, opticalCenter[1] - circleSize / 2)
        oval(0, 0, circleSize, circleSize)
        line((-circleSizeHalf, circleSizeHalf), (circleSize + circleSizeHalf, circleSizeHalf))
        line((circleSizeHalf, circleSize + circleSizeHalf), (circleSizeHalf, -circleSizeHalf))



size(signWidth + 36, signHeight + 36)



# Draw Horizontal Rectangle

def drawRects():
    horizontalRectWidth = signWidth - A * 2
    horizontalRectHeight = signHeight * .38

    verticalRectWidth = signWidth - B * 2
    verticalRectHeight = signHeight - (A * 2) - (A * .15)

    with savedState():

        fill(1)
        cmykStroke(0, 0, 0, 1)
        strokeWidth(4)

        rect(B, A + A * .15, verticalRectWidth, verticalRectHeight)
        rect(A, signHeight * .33, horizontalRectWidth, horizontalRectHeight)

        strokeWidth(0)
        rect(B, A + A * .15, verticalRectWidth, verticalRectHeight)
        rect(A, signHeight * .33, horizontalRectWidth, horizontalRectHeight)

        strokeWidth(1)
        lineDash((signWidth - B * 2) / 100, (signWidth - B * 2) / 100)
        translate(((signWidth - B * 2) / 100) / 2, 0)
        line((B, signHeight * .33 - 1), (signWidth - B, signHeight * .33 - 1))
        line((B, signHeight * .71 + 1), (signWidth - B, signHeight * .71 + 1))


# Draw Vertical Rectangle

translate(18, 18)
fill()
cmykStroke(0, 0, 0, 1)
rect(0, 0, signWidth, signHeight)
drawRects()
drawopticalCenter()


saveImage("sheet-02.pdf")
