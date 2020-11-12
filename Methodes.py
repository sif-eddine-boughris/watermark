
import numpy as np
from PIL import Image


def imageSize(image): #méthode qui calcule la taille de l'image
    size = image.shape[0] * image.shape[1]
    return size

def openImage(image):  #méthode pour ouvrir une image
    imageRGB = Image.open(image)
    return imageRGB

def openGrayScaled(image): #méthode pour ouvrir une image et la convertir en NDG
    imageNDG = Image.open(image).convert('L')
    return imageNDG

def convertToArray(image): #méthode pour convertir une image en matrice
    im = np.array(image)
    return im

def showImage(name,image):  #méthode pour afficher une image
    IMG = Image.fromarray(image)
    #IMG.save("résultats.jpg")
    IMG.show()



def calcHistogram(image): #méthode qui calcule l'histogramme d'une image
    histogram=[]
    for i in range (0,256):
        histogram.append(0)

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            histogram[image[i,j]]=histogram[image[i,j]]+1
    print("L'histogramme : ",histogram)
    return histogram

def calcWithinClassVariance(threshold,hist,Size): #méthode qui reçoit comme paramètres un seuil, l'histogramme d'une image et la taille et retourne le within Class Variance
    S1 = 0
    S2 = 0
    S3 = 0
    if(threshold==0):
        weightBackground=0
        varienceBackground=0
    else:
        for i in range(0, threshold):
            S1 = S1 + hist[i]
            S2 = S2 + hist[i] * i
        weightBackground = S1 / Size
        if (S1 == 0):  # cas de division par 0
            varienceBackground = 0
        else:
            MeanBackground = S2 / S1
            for i in range(0, threshold):
                S3 = S3 + ((i - MeanBackground) * (i - MeanBackground) * hist[i])

            varienceBackground = S3 / S1

    S1=0
    S2=0
    S3=0
    for i in range(threshold,256):
        S1 = S1 + hist[i]
        S2 = S2 + hist[i]*i

    weightForeground = S1 / Size
    if  (S1==0):        #cas de division par 0
        varienceForeground = 0
    else:
        MeanForeground = S2 / S1

        for i in range(threshold, 256):
            S3 = S3 + ((i - MeanForeground) * (i - MeanForeground) * hist[i])
        varienceForeground = S3 / S1
    withinClassVariance = weightBackground*varienceBackground + weightForeground*varienceForeground

    return withinClassVariance

def variancesTable(hist,size): #méthode qui calcule les within Class Variances pour chaque seuil de 0 à 255, et retourne une liste de 256 variances
    variances = []
    for i in range(0,256):
        variances.append(0)

    for i in range(0,256):
        variances[i] = calcWithinClassVariance(i,hist,size)

    return variances

def varianceMin(varianceTable): #méthode qui calcule la valeur minimale de la liste des variances, et retourne le seuil correspondent
    min=varianceTable[0]
    t=0
    for i in range (1,256):
       if(min> varianceTable[i]):
           min= varianceTable[i]
           t=i
    return t

def convertToBinary(t,img):  #méthode pour convertir une image en binaire avec un seuil t
    for i in range (img.shape[0]):
        for j in range(img.shape[1]):
            if(img[i,j]>= t):
                img[i,j]=255
            else:
                img[i,j]=0
    return img

def saveImage(name,image): #méthode qui sauvegarde une image dans le répertoire du projet
    Image.fromarray(image).save(name)


def otsuMethod(imageName,newImageName): #la methode principale d'Otsu
    image1 = openGrayScaled(imageName) #appel à la méthode pour ouvrir une image et la convertir en NDG
    image = convertToArray(image1)  #appel à la méthode pour convertir l'image en matrice
    size = imageSize(image)             #appel à la méthode qui calcule la taille de l'image
    histogram = calcHistogram(image)      #appel à la méthode qui calcule l'histogramme de l'image
    variances = variancesTable(histogram, size)     #appel à la méthode qui calcule les variances pour chaque seuil
    threshold = varianceMin(variances)             #appel à la méthode qui retourne le seuil
    print("le seuil = ",threshold)
    img = convertToBinary(threshold, image)         #appel à la méthode qui transforme l'image en binaire
    image2 = openImage(imageName)
    imageOriginal = convertToArray(image2)
    showImage('Original',imageOriginal)
    showImage('otsu', img)
    saveImage(newImageName, img)



