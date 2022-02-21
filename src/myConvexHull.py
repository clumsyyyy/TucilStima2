class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def findMinAbs(PointsList):
    min = PointsList[0]
    for i in range(len(PointsList)):
        if PointsList[i].x < min.x:
            min = PointsList[i]
    return min

def findMaxAbs(PointsList):
    max = PointsList[0]
    for i in range(len(PointsList)):
        if PointsList[i].x > max.x:
            max = PointsList[i]
    return max

def determinant(p1, p2, p3):
    return ((p1.x * p2.y) + (p3.x * p1.y) + (p2.x * p3.y) 
            - (p3.x * p2.y) - (p1.x * p3.y) - (p2.x * p1.y))
    
def distance(p1, p2, p3):
    return abs((p3.y - p1.y) * (p2.x - p1.x) - (p2.y - p1.y) * (p3.x - p1.x))
    
# fungsi untuk membagi list menjadi dua list sesuai dengan posisi determinan dan garis
# return dua buah list
def divideList(PointsList, minAbs, maxAbs, flag):
    leftSide = []
    rightSide = []
    for i in range(len(PointsList)):
        if (PointsList[i].x != minAbs.x and PointsList[i].x != maxAbs.x):
            if (determinant(minAbs, maxAbs, PointsList[i]) > 0):
                leftSide.append(PointsList[i])
            if (determinant(minAbs, maxAbs, PointsList[i]) < 0):
                rightSide.append(PointsList[i])

    # titik antara garis tidak bisa untuk membuat convex hull, abaikan
    if (flag > 0):
        return leftSide
    elif (flag < 0):
        return rightSide
    else:
        return leftSide, rightSide

def findPMax(PointsList, minAbs, maxAbs):
    currentDistance = 0
    maxDistance = 0
    index = 0
    for i in range(len(PointsList)):
        currentDistance = distance(minAbs, maxAbs, PointsList[i])
        if currentDistance > maxDistance:
            maxDistance = currentDistance
            index = i
    return PointsList[index]


def divideLeft(PointsList, minAbs, maxAbs):
    temp = []
    if len(PointsList) == 0: #basis apabila list kosong
        return []
    else:
        pMax = findPMax(PointsList, minAbs, maxAbs)
        temp.append(pMax)
        temp1 = divideLeft(divideList(PointsList, minAbs, pMax, 1), minAbs, pMax)
        if (len(temp1) > 0):
            for x in temp1:
                temp.append(x)
        temp2 = divideLeft(divideList(PointsList, pMax, maxAbs, 1), pMax, maxAbs)
        if (len(temp1) > 0):
            for x in temp2:
                temp.append(x)
        return temp
    
def divideRight(PointsList, minAbs, maxAbs):
    temp = []
    if len(PointsList) == 0: #basis apabila list kosong
        return []
    else:
        pMax = findPMax(PointsList, minAbs, maxAbs)
        temp.append(pMax)
        temp1 = divideRight(divideList(PointsList, minAbs, pMax, -1), minAbs, pMax)
        if (len(temp1) > 0):
            for x in temp1:
                temp.append(x)
        temp2 = divideRight(divideList(PointsList, pMax, maxAbs, -1), pMax, maxAbs)
        if (len(temp1) > 0):
            for x in temp2:
                temp.append(x)
        return temp

# fungsi yang akan dipanggil di main
# menerima list of points dan mengembalikan list of convex hull
def ConvexHull(listOfPoints):
    mergedList = []
    PointsList = []
    
    # membuat list yang berisi objectPoint
    for i in range(len(listOfPoints)):
        PointsList.append(Point(listOfPoints[i][0], listOfPoints[i][1]))
    
    # bubble sort berdasarkan koordinat x
    for i in range(len(PointsList) - 1):
        for j in range(len(PointsList) - i - 1):
            if (PointsList[j].x > PointsList[j + 1].x):
                PointsList[j], PointsList[j + 1] = PointsList[j + 1], PointsList[j]
    
    # mencari nilai absis minimum dan maksimum untuk
    # mendapatkan garis yang membagi points menjadi 2 bagian
    minAbs = findMinAbs(PointsList)
    maxAbs = findMaxAbs(PointsList)
    mergedList.append(minAbs)
    mergedList.append(maxAbs)
    leftSide, rightSide = divideList(PointsList, minAbs, maxAbs, 0)
    leftRes = divideLeft(leftSide, minAbs, maxAbs)
    rightRes = divideRight(rightSide, minAbs, maxAbs)
    
    for x in leftRes:
        mergedList.append(x)
    for x in rightRes:
        mergedList.append(x)
    mergedX = []
    mergedY = []
    for i in range(len(mergedList)):
        mergedX.append(float(mergedList[i].x))
        mergedY.append(float(mergedList[i].y))
    return [mergedX, mergedY]
