import matplotlib.pyplot as plt
import pandas as pd
import random
from sklearn import datasets
from myConvexHull.process import Convex
from scipy.spatial import ConvexHull

print("\nDriver for the myConvexHull Library")
print("using datasets from the sklearn library")
ConvexObj = Convex()

while True:
    #input opsi dataset dari library sklearn
    print("\n")
    print("Choose your dataset: ")
    print("1. Iris dataset")
    print("2. Wine dataset")
    print("3. Digits dataset")
    print("4. Breast cancer dataset")


    option = int(input("Input your option (0 to exit)\n>>> "))
    while (option not in range(0, 5)):
        print("Invalid input! Try again.\n")
        option = int(input("Input your option >>> "))
        
    if (option == 1):
        data = datasets.load_iris()
    elif (option == 2):
        data = datasets.load_wine()
    elif option == 3:
        data = datasets.load_digits()
    elif option == 4:
        data = datasets.load_breast_cancer()
    elif option == 0:
        print("Exiting program...\n")
        break
    
    # pemanggilan ddataset yang diinginkan
    df = pd.DataFrame(data.data, columns = data.feature_names)
    df['Target'] = pd.DataFrame(data.target)

    
    # output kolom yang tersedia
    print("\nAvailable columns:")
    for i in range(len(df.columns) - 1):
        print("{}. {}".format(i, df.columns[i]))

    print("Note: the y-column taken would be the column right next to the inputted column!")
    
    # input kolom menandakan kolom x, kolom y adalah input kolom + 1
    cols = int(input("Input your column (max: {}): ".format(len(df.columns) - 3)))
    while (cols + 1 >= len(df.columns) - 1):
        print("Invalid input! Try again.\n")
        cols = int(input("Input your column (max: {}): ".format(len(df.columns) - 3)))
        
    title = data.feature_names[cols] + " vs " + data.feature_names[cols + 1]
    print("Generating convex hull for {}...".format(title))


    plt.figure(figsize = (10, 6))
    plt.title(title + ' (myConvexHull)')
    plt.xlabel(data.feature_names[cols])
    plt.ylabel(data.feature_names[cols + 1])

    colors = ['b', 'r', 'g']
    
    # Penggunaan library myConvexHull
    for i in range(len(data.target_names)):
        # pengambilan data dari kolom cols dengan kolom yang bersebelahan
        bucket = df[df['Target'] == i].iloc[:, [cols, cols + 1]].values
        
        # pemanggilan fungsi ConvexHull
        hull = ConvexObj.ConvexHull(bucket)
        
        # generator warna random untuk plot dengan kategori di atas 3
        if (i >= len(colors)):
            tempColor = random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)
        else:
            tempColor = colors[i]
        
        # generasi plot
        plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i], color = tempColor)
        
        # memasukkan data dari hasil eksekusi fungsi ConvexHull
        # - hull[0] = array berisi titik x
        # - hull[1] = array berisi titik y
        # untuk setiap i, hull[0][i], hull[1][i] adalah pasangan titik (x, y)
        plt.plot(hull[0], hull[1], color = tempColor)
    plt.legend()
    plt.show()


    # Perbandingan menggunakan library SciPy
    plt.figure(figsize = (10, 6))
    plt.title(title + ' (SciPy)')
    plt.xlabel(data.feature_names[cols])
    plt.ylabel(data.feature_names[cols + 1])

    scolors = ["c", "m", "y"]
    for i in range(len(data.target_names)):
        
        # pemanggilan data dengan metode yang sama seperti library myConvexHull
        # inisialisasi funsi berbeda
        bucket = df[df['Target'] == i].iloc[:, [cols, cols + 1]].values
        hull = ConvexHull(bucket)
        
        # generator warna random untuk plot dengan kategori di atas 3
        if (i >= len(scolors)):
            tempColor = random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)
        else:
            tempColor = scolors[i]
        # generasi plot
        plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i], color = tempColor)
        # memasukkan data hasil eksekusi fungsi ConvexHull
        for simplex in hull.simplices:
            plt.plot(bucket[simplex, 0], bucket[simplex, 1], color = tempColor)
    plt.legend()
    plt.show()
