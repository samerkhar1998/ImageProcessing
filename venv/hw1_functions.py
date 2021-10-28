import glob
import cv2
import numpy
import numpy as np
import matplotlib.pyplot as plt
import math


def print_IDs():
    print("209050202+208517631\n")

def contrastEnhance(im,Range):

    a = (Range[1]-Range[0]) / (np.amax(im) - np.amin(im))
    b = Range[0] - a * np.amin(im)

    nim = np.array(a * np.array(im) + b)

    return nim, a,b

def showMapping(old_range, a, b):
    imMin = np.min(old_range)
    imMax = np.max(old_range)
    x = np.arange(imMin, imMax+1, dtype=np.float)
    y = a * x + b
    plt.figure()
    plt.plot(x, y)
    plt.xlim([0, 255])
    plt.ylim([0, 255])
    plt.title('contrast enhance mapping')

def minkowski2Dist(im1,im2):# p=2 -> Euclidean distance
    if(np.size(im1) != np.size(im2)):
        print("images are not in the same size, minkowski2Dist cant calculate!!!!!!")
        return 0
    hist1,_ = np.histogram(im1, bins = 256, range=(0,255)) #histogram for first image
    hist2,_ = np.histogram(im2, bins = 256, range=(0,255)) #histogram for second image

    return math.sqrt(np.sum((np.square(hist1- hist2))))# first distance between two pix then do square for each element in the new hist
                                                       # then sum all the elements all together then return the sqr for the sum.

def meanSqrDist(im1, im2):

    return np.mean(np.square(np.array(im1) - np.array(im2)))

def sliceMat(im):

    rows = len(im)
    columns = len(im[0])
    numPixel = rows*columns
    SL = np.zeros((256,numPixel),bool)

    for i in range(0,255):
         SL[i] = np.ravel(im) == i

    return np.transpose(SL)

def SLTmap(im1, im2):
    SLim1 = np.transpose(sliceMat(im1))
    TM = np.arange(256,dtype=float)

    for i in range(0,256):
        if len(np.ravel(im2)[np.where(SLim1[i] == True)]) != 0 :
            TM[i] = np.average(np.ravel(im2)[np.where(SLim1[i] == True)])

    return mapImage(im1, TM), TM

def mapImage (im,tm):
    TMim = im

    for i in range(0,256):
        np.ravel(TMim)[np.ravel(im) == i] = tm[i]

    return  TMim

def sltNegative(im):

    return

def sltThreshold(im, thresh):
    return