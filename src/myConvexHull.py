class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
# fungsi untuk menentukan orientasi antara tiga buah titik
# return string yang menandakan orientasi tiga buah titik
def orientationOf(a, b, c):
    slope = (b.y - a.y)*(c.x - b.x) - (b.x - a.x)*(c.y - b.y)
    
    if (slope > 0):
        return "CLOCKWISE" #1
    elif (slope == 0):
        return "COLINEAR" #0
    else:
        return "COUNTERCLOCKWISE" #-1
    
def divideList(PointsList):
    length = len(PointsList)
    
    # apabila panjang list berukuran 5 atau kurang, langsung saja masukkan
    # ke dalam fungsi yang memproses bruteforce-nya
    if (length < 5):
        return bruteHull(PointsList)
    
    # jika tidak, lakukan proses pembagian list
    # karena list sudah terurut sesuai koordinat x, maka
    # pembagian dapat dilakukan dengan membagi koordinat
    # dari awal hingga tengah list dan tengah list hingga akhir
    leftPoints = []
    for i in range(length // 2):
        leftPoints.append(PointsList[i])
        
    rightPoints = []
    for i in range(length // 2, length):
        rightPoints.append(PointsList[i])

    # gunakan rekursi untuk membagi lagi list kiri dan kanan
    # merge kedua list tersebut berdasarkan tangent dari kedua titik
    leftPart = divideList(leftPoints)
    rightPart = divideList(rightPoints)
    return mergeList(leftPart, rightPart)

def mergeList(leftPoints, rightPoints):
    leftSize = len(leftPoints)
    rightSize = len(rightPoints)
    
    # cari titik paling kanan di sisi kiri
    # dan titik paling kiri di sisi kanan
    # wait bukannya kalo udah disort berarti 
    # leftmostIndex = 0, rightmostIndex = 0?
    rightmost = 0;
    for i in range(1, leftSize):
        if (leftPoints[i].x > leftPoints[rightmost].x):
            rightmost = i
        elif (leftPoints[i].x == leftPoints[rightmost].x):
            if (leftPoints[i].y < leftPoints[rightmost].y):
                rightmost = i  
            
            
    leftmost = 0;
    for i in range(1, rightSize):
        if (rightPoints[i].x < rightPoints[leftmost].x):
            leftmost = i
        elif (rightPoints[i].x == rightPoints[leftmost].x):
            if (rightPoints[i].y > rightPoints[leftmost].y):
                leftmost = i


    # proses pencarian convex hull
    leftUpperIdx = 0;
    rightUpperIdx = 0;
    
    for i in range(len(leftPoints)):
        if orientationOf(rightPoints[leftmost], leftPoints[rightmost], leftPoints[i]) == "COUNTERCLOCKWISE":
            leftUpperIdx = i
            break
    for i in range(len(rightPoints)):
        if orientationOf(leftPoints[rightmost], rightPoints[leftmost], rightPoints[i]) == "CLOCKWISE":
            rightUpperIdx = i
            break
    
    leftLowerIdx = 0;
    rightLowerIdx = 0;
    
    for i in range(len(rightPoints)):
        if orientationOf(leftPoints[rightmost], rightPoints[leftmost], rightPoints[i]) == "COUNTERCLOCKWISE":
            rightLowerIdx = i
            break
    for i in range(len(leftPoints)):
        if orientationOf(rightPoints[leftmost], leftPoints[rightmost], leftPoints[i]) == "CLOCKWISE":
            leftLowerIdx = i
            break
    
    # proses penggabungan list
    mergedPoints = []
    
    mergedPoints.append(leftPoints[leftUpperIdx])
    while (leftUpperIdx != leftLowerIdx):
        leftUpperIdx = (leftUpperIdx + 1) % len(leftPoints)
        mergedPoints.append(leftPoints[leftUpperIdx])

    mergedPoints.append(rightPoints[rightLowerIdx])
    while (rightLowerIdx != rightUpperIdx):
        rightLowerIdx = (rightLowerIdx + 1) % len(rightPoints)
        mergedPoints.append(rightPoints[rightLowerIdx])
        
        
    return mergedPoints
        
        
def bruteHull(PointsList):
    length = len(PointsList)
    if length < 3:
        return PointsList
    
    hull = []
    leftmost = 0;
    for i in range(1, length):
        if (PointsList[i].x < PointsList[leftmost].x):
            leftmost = i
        elif (PointsList[i].x == PointsList[leftmost].x):
            if (PointsList[i].y > PointsList[leftmost].y):
                leftmost = i
    
    temp = leftmost
    idx = 0
    while (True):
        hull.append(temp)
        # cari index yang membuat orientasi counterclockwise
        idx = (temp + 1) % length
        for i in range(length):
            if orientationOf(PointsList[temp], PointsList[i], PointsList[idx]) == "COUNTERCLOCKWISE":
                idx = i
                
        temp = idx
        if (temp == leftmost):
            break
    
    hullList = []
    for i in range(len(hull)):
        hullList.append(PointsList[hull[i]])
    return hullList
        
    
    
# fungsi yang akan dipanggil di utama
# menerima list of points dan mengembalikan list of convex hull
def ConvexHull(listOfPoints):
    PointsList = []
    
    # membuat list yang berisi objectPoint
    for i in range(len(listOfPoints)):
        PointsList.append(Point(listOfPoints[i][0], listOfPoints[i][1]))
    
    # bubble sort berdasarkan koordinat x
    for i in range(len(PointsList) - 1):
        for j in range(len(PointsList) - i - 1):
            if (PointsList[j].x > PointsList[j + 1].x):
                PointsList[j], PointsList[j + 1] = PointsList[j + 1], PointsList[j]
    # memasukkan list tersebut ke dalam fungsi divideList
    
    mergedList = divideList(PointsList)
    return mergedList
    

     