import cv2
import numpy
import numpy as np
import matplotlib.pyplot as plt
import math


def print_IDs():
    print("209050202+208517631\n")


def contrastEnhance(im,range):
    # new(x,y) = a (old(xy))-> we want new(a,y) to be 255 -> a = new(x,y)/old(x,y) -> a = 255 / (y-x)
    # y=ax+b -> y=0(to calculate b in linear fun) -> in case y=0 wich means new(x,y) = y sow we know that old(x,y) is the old minimum gray
    # so b = -ax -> b = -a*(oldMinimumGray)

    a = 255 / (range[1] - range[0])
    b = -1 * a * range[0]

    nim = a*im + b

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
    #halaaaaaaaaaaaaa


def minkowski2Dist(im1,im2):# p=2 -> Euclidean distance


    hist1 = cv2.calcHist([im1], [0], None, [256], [0, 256])#histogram for first image
    hist2 = cv2.calcHist([im2], [0], None, [256], [0, 256])#histogram for second image
    #explanaition on cv2.calcHist:
    # parameters:
    # 1 : image need to be in a list
    # 2 : [0] for computing a histogram of a grayscaleimage,to compute for all three (red,green,blue) we need to put[0,1,2]
    # 3 : here we can supply a mask,if a mask is provided, a histogram will be computed for masked pixels only.
    #    in our case there is no mask so we put 'None'
    # 4 : This is the number of bins we want to use when computing a histogram.
    #    Again, this is a list, one for each channel we are computing a histogram for. The bin sizes do not all have to be the same
    # 5 : The range of possible pixel values. Normally, this is [0, 256]
    #    (that is not a typo — the ending range of the cv2.calcHist function is non-inclusive so you’ll want to provide a value of 256 rather than 255) for each channel,
    #    but if you are using a color space other than RGB [such as HSV], the ranges might be different.)

    return math.sqrt(np.sum((np.square(hist1- hist2))))#first distance between two pix then do square for each element in the new hist
                                                       #then sum all the elements all together then return the sqr for the sum.


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
    # TODO: implement fucntion
    return mapImage(im1, TM), TM


def mapImage (im,tm):
    # TODO: implement fucntion
    return TMim


def sltNegative(im):
	# TODO: implement fucntion - one line
    return


def sltThreshold(im, thresh):
    # TODO: implement fucntion
    return