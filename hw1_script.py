import cv2.cv2
import numpy as np

from hw1_functions import *

if __name__ == "__main__":
    # feel free to add/remove/edit lines


    path_image = r'C:\Users\Samer\OneDrive - University of Haifa\university-samer\image_Proccessing\hw1\Images\darkimage.tif'
    darkimg = cv2.imread(path_image)
    darkimg_gray = cv2.cvtColor(darkimg, cv2.COLOR_BGR2GRAY)

    path_image2 = r'C:\Users\Samer\OneDrive - University of Haifa\university-samer\image_Proccessing\hw1\Images\RealLena.tif'
    darkimg2 = cv2.imread(path_image2)
    darkimg_gray2 = cv2.cvtColor(darkimg2, cv2.COLOR_BGR2GRAY)

    print("Start running script  ------------------------------------\n")
    print_IDs()

    # print("a ------------------------------------\n")
    # range = [100, 150]
    # enhanced_img, a, b = contrastEnhance(darkimg_gray,range)  # add parameters
    #
    # # display images
    # plt.figure()
    # plt.subplot(1, 2, 1)
    # plt.imshow(darkimg)
    # plt.title('original')
    #
    # plt.subplot(1, 2, 2)
    # plt.imshow(enhanced_img, cmap='gray', vmin=0, vmax=255)
    # plt.title('enhanced contrast')
    #
    # # print a,b
    # print("a = {}, b = {}\n".format(a, b))
    #
    # # display mapping
    # showMapping(range,a,b)  # add parameters
    #
    # print("b ------------------------------------\n")
    # enhanced2_img, a, b = contrastEnhance(enhanced_img,[0,255])  # add parameters
    # # enhanced2_img = cv2.cv2.cvtColor(enhanced2_img,cv2.cv2.COLOR_BGR2GRAY)
    # # print a,b
    # print("enhancing an already enhanced image\n")
    # print("a = {}, b = {}\n".format(a, b))
    #
    # # TODO: display the difference between the two image (Do not simply display both images)--done!
    #
    # plt.figure()
    # plt.subplot(1, 2, 1)
    # difference = enhanced2_img - enhanced_img
    # plt.imshow(enhanced2_img, cmap='gray', vmin=0, vmax=255)
    # plt.title('max contrast enhance')
    #
    # plt.subplot(1, 2, 2)
    # difference = enhanced2_img - enhanced_img
    # plt.imshow(difference,cmap='gray', vmin=0, vmax=255)
    # plt.title('Diff between enhanced1 and max enhance')

    # print("c ------------------------------------\n")
    # mdist = minkowski2Dist(darkimg_gray,darkimg_gray)  # add parameters
    # print("Minkowski dist between image and itself\n")
    # print("d = {}\n".format(mdist))

    # TODO:
    # implement the loop that calculates minkowski distance as function of increasing contrast
    # max = np.amax(darkimg_gray)
    # min = np.amin(darkimg_gray)
    # step = (max - min)/20
    # contrast = []
    # dists = []
    # for i in range(1,21):
    #     newIm, _, _a= contrastEnhance(darkimg_gray, [min, min + i * step])
    #     contrast.append(i*step)
    #     dists.append(minkowski2Dist(darkimg_gray, newIm))
    #
    #
    # plt.figure()
    # plt.plot(contrast, dists)
    # plt.xlabel("contrast")
    # plt.ylabel("distance")
    # plt.title("Minkowski distance as function of contrast")

    # print("d ------------------------------------\n")
    #
    # d = np.sum(np.ravel(darkimg_gray) - np.matmul(sliceMat(darkimg_gray),np.arange(0,256)))# computationally prove that sliceMat(im) * [0:255] == im
    # print("{}".format(d))
    #
    # print("e ------------------------------------\n")
    #
    # d = np.sum(np.ravel(darkimg_gray) - np.matmul(sliceMat(darkimg_gray2),np.arange(0,256))) # computationally compare
    # print("sum of diff between image and slices*[0..255] = {}".format(d))
    #
    # # then display
    # plt.figure()
    # plt.subplot(1, 2, 1)
    # plt.imshow(darkimg)
    # plt.title("original image")
    # plt.subplot(1, 2, 2)
    # TMim, TM = SLTmap(darkimg_gray, darkimg_gray2)
    # plt.imshow(TMim, cmap='gray', vmin=0, vmax=255)
    # plt.title("tone mapped")

    # print("f ------------------------------------\n")
    # negative_im = sltNegative(darkimg_gray)
    # plt.figure()
    # plt.imshow(negative_im, cmap='gray', vmin=0, vmax=255)
    # plt.title("negative image using SLT")

    # print("g ------------------------------------\n")
    # thresh = 120  # play with it to see changes
    # lena = cv2.imread(r"Images\\RealLena.tif")
    # lena_gray = cv2.cvtColor(lena, cv2.COLOR_BGR2GRAY)
    # thresh_im = sltThreshold()  # add parameters
    #
    # plt.figure()
    # plt.imshow(thresh_im, cmap='gray', vmin=0, vmax=255)
    # plt.title("thresh image using SLT")
    #
    # print("h ------------------------------------\n")
    # im1 = lena_gray
    # im2 = darkimage
    # SLTim =  # TODO
    #
    # # then print
    # plt.figure()
    # plt.subplot(1, 3, 1)
    # plt.imshow(im1)
    # plt.title("original image")
    # plt.subplot(1, 3, 2)
    # plt.imshow(SLTim, cmap='gray', vmin=0, vmax=255)
    # plt.title("tone mapped")
    # plt.subplot(1, 3, 3)
    # plt.imshow(im2, cmap='gray', vmin=0, vmax=255)
    # plt.title("tone mapped")
    #
    # d1 =  # mean sqr dist between im1 and im2
    # d2 =  # mean sqr dist between mapped image and im2
    # print("mean sqr dist between im1 and im2 = {}\n".format(d1))
    # print("mean sqr dist between mapped image and im2 = {}\n".format(d2))
    #
    # print("i ------------------------------------\n")
    # # prove comutationally
    # d =  # TODO:
    # print(" {}".format(d))

    plt.show()