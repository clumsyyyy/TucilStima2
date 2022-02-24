import math

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

def findAngle(minAbs, maxAbs, pMax):
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
    index = 0
    for i in range(len(PointsList)):
        currentDistance = distance(minAbs, maxAbs, PointsList[i])
        if currentDistance > maxDistance or (currentDistance == maxDistance and
            findAngle(minAbs, maxAbs, PointsList[i]) > findAngle(minAbs, maxAbs, PointsList[index])):
            maxDistance = currentDistance
            index = i
    return PointsList[index]