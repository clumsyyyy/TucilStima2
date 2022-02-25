
import myConvexHull.utils as ut

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
            if (((PointsList[i].x > minAbs.x) or (PointsList[i].x == minAbs.x and PointsList[i].y < minAbs.y))  
                and ((PointsList[i].x < maxAbs.x) or (PointsList[i].x == maxAbs.x and PointsList[i].y < maxAbs.y))):
                if (ut.isDeterminantPositive(minAbs, maxAbs, PointsList[i])):
                    leftSide.append(PointsList[i])
                if (not ut.isDeterminantPositive(minAbs, maxAbs, PointsList[i])):
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
            pMax = ut.findPMax(PointsList, minAbs, maxAbs)
            PointsList.remove(pMax)
            temp.append(pMax)
            leftTemp = self.divideLeft(self.divideList(PointsList, minAbs, pMax, 1), minAbs, pMax)
            if (len(leftTemp) > 0):
                for point in leftTemp:
                    PointsList.remove(point)
                    temp.append(point)
            rightTemp = self.divideLeft(self.divideList(PointsList, pMax, maxAbs, 1), pMax, maxAbs)
            if (len(rightTemp) > 0):
                for point in rightTemp:
                    PointsList.remove(point)
                    temp.append(point)
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
            pMax = ut.findPMax(PointsList, minAbs, maxAbs)
            PointsList.remove(pMax)
            temp.append(pMax)
            leftTemp = self.divideRight(self.divideList(PointsList, minAbs, pMax, -1), minAbs, pMax)
            if (len(leftTemp) > 0):
                for point in leftTemp:
                    PointsList.remove(point)
                    temp.append(point)
            rightTemp = self.divideRight(self.divideList(PointsList, pMax, maxAbs, -1), pMax, maxAbs)
            if (len(rightTemp) > 0):
                for point in rightTemp:
                    PointsList.remove(point)
                    temp.append(point)
            return temp

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
        for i in range(len(leftRes)):
            mergedList.append(leftRes[i])
            
        mergedList.append(maxAbs)
        for i in range(len(rightRes)):
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
            PointsList.append(ut.Point(listOfPoints[i][0], listOfPoints[i][1]))
        
        # bubble sort berdasarkan koordinat x
        for i in range(len(PointsList) - 1):
            for j in range(len(PointsList) - i - 1):
                if (PointsList[j].x > PointsList[j + 1].x):
                    PointsList[j], PointsList[j + 1] = PointsList[j + 1], PointsList[j]
        
        # mencari nilai absis minimum dan maksimum untuk
        # mendapatkan garis yang membagi points menjadi 2 bagian
        minAbs = PointsList[0]
        maxAbs = PointsList[len(PointsList) - 1]
        PointsList.remove(minAbs)
        PointsList.remove(maxAbs)        

        leftSide, rightSide = self.divideList(PointsList, minAbs, maxAbs, 0)
        leftRes = self.divideLeft(leftSide, minAbs, maxAbs)
        rightRes = self.divideRight(rightSide, minAbs, maxAbs)
        return self.mergeList(leftRes, rightRes, minAbs, maxAbs)
    