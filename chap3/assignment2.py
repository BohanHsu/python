# calculate the volume of one plywood
# @param height: height of plywood
# @param width: width of plywood
# @param thickness: thickness of plywood
# @return the volume of plywood
def calcVolume(height, width, thickness):
    volume = height * width * thickness
    return volume

lengthA = 5.0
widthA = 3.0
thicknessA = 1.0 / 12.0
quantityA = 12
totalVolumeInCodeA = quantityA * calcVolume(lengthA, widthA, thicknessA)

lengthB = 5.0
widthB = 5.0
thicknessB = 1.0 / 12.0
quantityB = 20
totalVolumeInCodeB = quantityB * calcVolume(lengthB, widthB, thicknessB)

lengthC = 6.0
widthC = 4.0
thicknessC = 1.0 / 24.0
quantityC = 10
totalVolumeInCodeC = quantityC * calcVolume(lengthC, widthC, thicknessC)

totalVolume = totalVolumeInCodeA + totalVolumeInCodeB + totalVolumeInCodeC

print "Total volume in code A:", totalVolumeInCodeA
print "Total volume in code B:", totalVolumeInCodeB
print "Total volume in code C:", totalVolumeInCodeC
print ""
print "Total volume of A, B, and C:", totalVolume
