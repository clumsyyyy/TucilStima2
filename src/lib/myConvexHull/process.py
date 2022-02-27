from myConvexHull.utils import *

class Convex(object):        
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
            # kondisi untuk menambahkan titik adalah apabila:
            # - titik mempunyai nilai absis antara minAbs dan maxAbs
            # - titik mempunyai nilai absis sama dengan minAbs tapi ordinat lebih tinggi
            # - titik mempunyai nilai absis sama dengan minAbs tapi ordinat lebih rendah
            if (((PointsList[i].x > minAbs.x) or (PointsList[i].x == minAbs.x and PointsList[i].y > minAbs.y))  
                and ((PointsList[i].x < maxAbs.x) or (PointsList[i].x == maxAbs.x and PointsList[i].y < maxAbs.y))):
                
                # fungsi akan menambahkan point ke leftSide apabila determinan positif,
                # sebaliknya akan menambahkan ke rightSide apabila determinan negatif
                if (isDeterminantPositive(minAbs, maxAbs, PointsList[i])):
                    leftSide.append(PointsList[i])
                if (not isDeterminantPositive(minAbs, maxAbs, PointsList[i])):
                    rightSide.append(PointsList[i])
                

        # flag menunjukkan list mana yang akan dikembalikan
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
        if len(PointsList) == 0:    #basis, list kosong
            return []
        else:       #rekurens, pencarian titik pMax dan pemanggilan right secara rekursif
            pMax = findPMax(PointsList, minAbs, maxAbs)
            PointsList.remove(pMax) 
            
            # pemanggilan fungsi pembagian ke kiri secara rekurif
            # pembagian dilakukan secara konsisten dengan meninjau
            # bagian kiri dari garis yang dibentuk antara minAbs - pMax
            # dan pMax - maxAbs sampai list kosong
            leftTemp = self.divideLeft(self.divideList(PointsList, minAbs, pMax, 1), minAbs, pMax)
            rightTemp = self.divideLeft(self.divideList(PointsList, pMax, maxAbs, 1), pMax, maxAbs)
            return leftTemp + [pMax] + rightTemp
        
    def divideRight(self, PointsList, minAbs, maxAbs):
        '''
        Membagi list of points menjadi dua bagian berdasarkan determinan
        untuk bagian kanan dari garis awal. Fungsi ini akan melakukan
        pembagian secara rekursif sampai list kosong.
        Argumen fungsi:
            - PointsList: list of points yang akan dibagi
            - minAbs, maxAbs: titik dengan absis minimum/maksimum
        '''
        if len(PointsList) == 0:    #basis, list kosong
            return []
        else:       # rekursi, pencarian titik pMax dan pemanggilan left secara rekursif
            pMax = findPMax(PointsList, minAbs, maxAbs)
            PointsList.remove(pMax)
            
            # pemanggilan fungsi pembagian ke kanan secara rekurif
            # pembagian dilakukan secara konsisten dengan meninjau
            # bagian kanan dari garis yang dibentuk antara minAbs - pMax
            # dan pMax - maxAbssampai list kosong
            leftTemp = self.divideRight(self.divideList(PointsList, minAbs, pMax, -1), minAbs, pMax)
            rightTemp = self.divideRight(self.divideList(PointsList, pMax, maxAbs, -1), pMax, maxAbs)
            return leftTemp + [pMax] + rightTemp

    def mergeList(self, leftRes, rightRes, minAbs, maxAbs):
        '''
        FUNGSI MERGE
        Menggabungkan titik yang berada di dalam list leftRes dan rightRes
        (hasil divide and conquer) dengan titik absis minimum/maksimum.
        Argumen fungsi:
            - leftRes, rightRes: hasil dari divideLeft dan divideRight
            - minAbs, maxAbs: titik dengan absis minimum/maksimum
        '''
        mergedList = []
        # lakukan pengurutan terhadap leftRes dan rightRes
        leftRes = quickSort(leftRes)
        rightRes = quickSort(rightRes)

        # proses penggabungan list
        mergedList.append(minAbs)
        for i in range(len(leftRes)):
            mergedList.append(leftRes[i])
            
        mergedList.append(maxAbs)
        for i in range(len(rightRes) - 1, -1, -1):
            mergedList.append(rightRes[i])
        
        mergedList.append(mergedList[0])

        # pembagian list menjadi dua bagian, list x dan y
        # untuk dimasukkan ke plt.plot
        mergedX = [point.x for point in mergedList]
        mergedY = [point.y for point in mergedList]

        return [mergedX, mergedY]


    def ConvexHull(self, listOfPoints):
        '''
        Fungsi utama (saat pemanggilan)
        Menerima dataset dalam bentuk list dua dimensi (x, y)
        '''
        # membuat list yang berisi object Point
        PointsList = removeDupes(quickSort([Point(point[0], point[1]) for point in listOfPoints]))
        
        # mencari nilai absis minimum dan maksimum untuk
        # mendapatkan garis yang membagi points menjadi 2 bagian
        minAbs = PointsList[0]
        maxAbs = PointsList[len(PointsList) - 1]

        # pembagian list ke bagian kiri dan kanan garis
        leftSide, rightSide = self.divideList(PointsList[1:-1], minAbs, maxAbs, 0)
        
        # pemanggilan fungsi pembagian secara rekursif
        leftRes = self.divideLeft(leftSide, minAbs, maxAbs)
        rightRes = self.divideRight(rightSide, minAbs, maxAbs)
        
        # pemanggilan fungsi merging
        return self.mergeList(leftRes, rightRes, minAbs, maxAbs)