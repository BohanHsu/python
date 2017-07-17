# calculate the area of a rectangle and print out on screen
# @param length: length of the rectangle
# @param width: width of the rectangle
# @return: void
def calcRectArea(length, width):
    area = length * width
    print "length =", length, "width =", width, "area =", area

# calculate the perimeter of a rectangle and print out on screen
# @param length: length of the rectangle
# @param width: width of the rectangle
# @return: void
def calcRectPerim(length, width):
    perimeter = 2 * length + 2 * width
    print "length =", length, "width =", width, "perimeter =", perimeter


# print area and perimeter of rectangle (2,1)
calcRectArea(2,1)
calcRectPerim(2,1)

# print area and perimeter of rectangle (4,2)
calcRectArea(4,2)
calcRectPerim(4,2)

# print area and perimeter of rectangle (8,4)
calcRectArea(8,4)
calcRectPerim(8,4)
