import math

class Point:
    '''
    Class Point untuk merepresentasikan sebuah titik 
    dalam bidang dua-dimensi.
    '''
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def sameAs(self, p):
        return self.x == p.x and self.y == p.y

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

def findAngle(minAbs, maxAbs, pMax):
    '''
    Fungsi untuk mencari sudut pMax, minAbs, maxAbs
    menggunakan aturan cosinus
    '''
    aSide = (pMax.x - maxAbs.x) ** 2 + (pMax.y - maxAbs.y) ** 2
    bSide = (pMax.x - minAbs.x) ** 2 + (pMax.y - minAbs.y) ** 2
    cSide = (maxAbs.x - minAbs.x) ** 2 + (maxAbs.y - minAbs.y) ** 2
    cos = (aSide - bSide - cSide) / (-2 * (bSide ** 0.5) * (cSide ** 0.5))
    return math.acos(cos) * 180 / math.pi


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
    maxIndex = 0
    for i in range(0, len(PointsList)):

        currentDistance = distance(minAbs, maxAbs, PointsList[i])
        currentAngle = findAngle(minAbs, maxAbs, PointsList[i])
        maxAngle = findAngle(minAbs, maxAbs, PointsList[maxIndex])
        # syarat pembaruan pMax adalah apabila
        # - jarak terjauh lebih besar dari jarak sebelumnya
        # - atau jarak terjauh sama dengan jarak sebelumnya, tetapi 
        #   sudut pMax-minAbs-maxAbs lebih besar dibandingkan sudut sebelumnya
        if (currentDistance > maxDistance or (currentDistance == maxDistance and
            currentAngle > maxAngle)):
            maxDistance = currentDistance
            maxAngle = currentAngle
            maxIndex = i
    return PointsList[maxIndex]

def quickSort(PointsList):
    ''' 
    Fungsi untuk melakukan quicksort menggunakan list comprehension
    dalam Python
    Fungsi akan membagi PointsList menjadi pivot, bagian yang lebih kecil
    dari pivot, dan bagian yang lebih besar dari pivot, dan
    melakukan pemrosesan list secara rekursif hingga kosong
    '''

    if len(PointsList) == 0:
        return []
    else:
        pivot = PointsList[0]
        smaller = quickSort([point for point in PointsList[1:] if (point.x < pivot.x) or
                   (point.x == pivot.x and point.y < pivot.y)])
        bigger = quickSort([point for point in PointsList[1:] if (point.x > pivot.x) or
                  (point.x == pivot.x and point.y > pivot.y)])
        return smaller + [pivot] + bigger

def removeDupes(PointsList):
    '''
    Fungsi untuk menghapus points duplikat dari PointsList
    Argumen:
        - PointsList: list yang akan disaring
    '''
    PList = []
    for point in PointsList:
        i = 0
        found = False
        while (i < len(PointsList) and not found):
            if point.sameAs(PointsList[i]):
                break
            else:
                i += 1
        if not found:
            PList.append(point)
    return PList
