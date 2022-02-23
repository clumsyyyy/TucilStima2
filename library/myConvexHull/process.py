class Point:
    '''
    Class Point untuk merepresentasikan sebuah titik 
    dalam bidang dua-dimensi.
    '''
    def __init__(self, x, y):
        self.x = x
        self.y = y

def isDeterminantPositive(p1, p2, p3):
    '''
    Menghitung determinan antara dua buah titik (p1 dan p2)
    yang membentuk sebuah garis dan titik p3 untuk menentukan 
    letak sebuah titik relatif terhadap garis.
    - Determinan positif: titik berada pada sisi kiri relatif dari garis
    - Determinan negatif: titik berada pada sisi kanan relatif dari garis
    - Determinan nol: titik berada pada garis dan dapat diabaikan
    Argumen fungsi:
        - p1, p2: titik yang membentuk garis (absis minimum dan maksimum)
        - p3: titik yang dibandingkan
    '''
    det = ((p1.x * p2.y) + (p3.x * p1.y) + (p2.x * p3.y) 
            - (p3.x * p2.y) - (p1.x * p3.y) - (p2.x * p1.y))
    if (det > 0):
        return True
    if (det < 0):
        return False
    
def distance(p1, p2, p3):
    '''
    Menghitung jarak antara garis yang dibentuk p1 dan p2
    dengan titik p3.
    Argumen fungsi:
        p1, p2: titik yang membentuk garis (absis minimum dan maksimum)
        p3: titik yang dibandingkan
    '''
    A = p1.y - p2.y
    B = p2.x - p1.x
    C = p1.x * p2.y - p2.x * p1.y
    dist = abs((A * p3.x + B * p3.y + C) / ((A ** 2 + B ** 2) ** 0.5))
    return dist
    # return abs((p3.y - p1.y) * (p2.x - p1.x) - (p2.y - p1.y) * (p3.x - p1.x))
    
def findPMax(PointsList, minAbs, maxAbs):
    '''
    Fungsi untuk menentukan pMax, titik berjarak terjauh dari garis
    yang dibentuk minAbs dan maxAbs.
    Argumen fungsi:
        - PointsList: list of points yang akan dibagi
        - minAbs, maxAbs: titik dengan absis minimum/maksimum
    '''
    currentDistance = 0
    maxDistance = 0
    index = 0
    for i in range(len(PointsList)):
        currentDistance = distance(minAbs, maxAbs, PointsList[i])
        if currentDistance > maxDistance:
            maxDistance = currentDistance
            index = i
    return PointsList[index]

class Convex(object):
    def __init__(self):
        self.PointsList = []
        
    def divideList(self, PointsList, minAbs, maxAbs, flag):
        '''
        FUNGSI DIVIDE:
        Membagi list of points menjadi dua bagian berdasarkan determinan
        relatif terhadap garis yang dibentuk titik absis minimum dan maksimum.
        Titik yang mempunyai determinan positif terhadap garis dimasukkan ke
        list leftSide, sementara titik dengan determinan negatif dimasukkan ke
        list rightSide.
        Argumen fungsi:
            - PointsList: list of points yang akan dibagi
            - minAbs, maxAbs: titik dengan absis minimum/maksimum
            - flag: integer untuk menentukan list mana yang akan dikembalikan
            (beberapa kasus membutuhkan hanya list kiri / kanan)
        '''
        leftSide = []
        rightSide = []
        for i in range(len(PointsList)):
            if (((PointsList[i].x > minAbs.x) or (PointsList[i].x == minAbs.x and PointsList[i].y < minAbs.y))  
                and ((PointsList[i].x < maxAbs.x) or (PointsList[i].x == maxAbs.x and PointsList[i].y < maxAbs.y))):
                if (isDeterminantPositive(minAbs, maxAbs, PointsList[i])):
                    leftSide.append(PointsList[i])
                if (not isDeterminantPositive(minAbs, maxAbs, PointsList[i])):
                    rightSide.append(PointsList[i])

        if (flag > 0):
            return leftSide
        elif (flag < 0):
            return rightSide
        else:
            return leftSide, rightSide



    def divideLeft(self, PointsList, minAbs, maxAbs):
        '''
        Membagi list of points menjadi dua bagian berdasarkan determinan
        untuk bagian kiri dari garis awal. Fungsi ini akan melakukan
        pembagian secara rekursif sampai list kosong.
        Argumen fungsi:
            - PointsList: list of points yang akan dibagi
            - minAbs, maxAbs: titik dengan absis minimum/maksimum
        '''
        temp = []
        if len(PointsList) == 0: 
            return []
        else:
            pMax = findPMax(PointsList, minAbs, maxAbs)
            temp.append(pMax)
            temp1 = self.divideLeft(self.divideList(PointsList, minAbs, pMax, 1), minAbs, pMax)
            if (len(temp1) > 0):
                for x in temp1:
                    temp.append(x)
            temp2 = self.divideLeft(self.divideList(PointsList, pMax, maxAbs, 1), pMax, maxAbs)
            if (len(temp2) > 0):
                for x in temp2:
                    temp.append(x)
            return temp
        
    def divideRight(self, PointsList, minAbs, maxAbs):
        '''
        Membagi list of points menjadi dua bagian berdasarkan determinan
        untuk bagian kanan dari garis awal. Fungsi ini akan melakukan
        pembagian secara rekursif sampai list kosong.
        Argumen fungsi:
            - PointsList: list of points yang akan dibagi
            - minAbs, maxAbs: titik dengan absis minimum/maksimum
        '''
        temp = []
        if len(PointsList) == 0: #basis apabila list kosong
            return []
        else:
            pMax = findPMax(PointsList, minAbs, maxAbs)
            temp.append(pMax)
            temp1 = self.divideRight(self.divideList(PointsList, minAbs, pMax, -1), minAbs, pMax)
            if (len(temp1) > 0):
                for x in temp1:
                    temp.append(x)
            temp2 = self.divideRight(self.divideList(PointsList, pMax, maxAbs, -1), pMax, maxAbs)
            if (len(temp2) > 0):
                for x in temp2:
                    temp.append(x)
            return temp

    def mergeList(self, leftRes, rightRes, minAbs, maxAbs):
        '''
        Menggabungkan titik yang berada di dalam list leftRes dan rightRes
        (hasil divide and conquer) dengan titik absis minimum/maksimum.
        Argumen fungsi:
            - leftRes, rightRes: hasil dari divideLeft dan divideRight
            - minAbs, maxAbs: titik dengan absis minimum/maksimum
        '''
        mergedList = []
        # sort leftRes ascending, sort rightRes descending
        for i in range(len(leftRes) - 1):
            for j in range(len(leftRes) - i - 1):
                if (leftRes[j].x > leftRes[j + 1].x):
                    leftRes[j], leftRes[j + 1] = leftRes[j + 1], leftRes[j]
                    
        for i in range(len(rightRes) - 1):
            for j in range(len(rightRes) - i - 1):
                if (rightRes[j].x < rightRes[j + 1].x):
                    rightRes[j], rightRes[j + 1] = rightRes[j + 1], rightRes[j]
                    
        mergedList.append(minAbs)
        # print("minAbs: ", minAbs.x, minAbs.y)
        for i in range(len(leftRes)):
            # print("leftRes {}".format(i), leftRes[i].x, leftRes[i].y)
            mergedList.append(leftRes[i])
            
        mergedList.append(maxAbs)
        # print("maxAbs", maxAbs.x, maxAbs.y)
        for i in range(len(rightRes)):
            # print("rightRes {}".format(i), rightRes[i].x, rightRes[i].y)
            mergedList.append(rightRes[i])
        
        mergedList.append(mergedList[0])

        mergedX = []
        mergedY = []
        
        for i in range(len(mergedList)):
            mergedX.append(float(mergedList[i].x))
            mergedY.append(float(mergedList[i].y))
        return [mergedX, mergedY]


    def ConvexHull(self, listOfPoints):
        '''
        Fungsi utama (saat pemanggilan)
        Menerima dataset dalam bentuk list dua dimensi (x, y)
        '''
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
        minAbs = PointsList[0]
        maxAbs = PointsList[len(PointsList) - 1]
        

        leftSide, rightSide = self.divideList(PointsList[1:-2], minAbs, maxAbs, 0)
        leftRes = self.divideLeft(leftSide, minAbs, maxAbs)
        rightRes = self.divideRight(rightSide, minAbs, maxAbs)
        return self.mergeList(leftRes, rightRes, minAbs, maxAbs)