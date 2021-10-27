import numpy as np
from hw1_functions import *

if __name__ == "__main__":
    # feel free to add/remove/edit lines
    path_image = r'C:\Users\Samer\OneDrive - University of Haifa\university-samer\image_Proccessing\hw1\Images\darkimage.tif'
    darkimg = cv2.imread(path_image)
    darkimg_gray = cv2.cvtColor(darkimg, cv2.COLOR_BGR2GRAY)

    path_image2 = r'C:\Users\Samer\OneDrive - University of Haifa\university-samer\image_Proccessing\hw1\Images\fruit.tif'
    darkimg2 = cv2.imread(path_image2)
    darkimg_gray2 = cv2.cvtColor(darkimg2, cv2.COLOR_BGR2GRAY)

    # print("a ------------------------------------\n")
    # # contrastEnhance(darkimg_gray, range=[0, 255])
    # range = [np.amin(darkimg_gray),np.amax(darkimg_gray)]
    # enhanced_img, a, b = contrastEnhance(darkimg_gray,range)  # add parameters


    # display images
    # plt.figure()
    # plt.subplot(1, 2, 1)
    # plt.imshow(darkimg)
    # plt.title('original')
    #
    # plt.subplot(1, 2, 2)
    # plt.imshow(enhanced_img, cmap='gray')
    # plt.title('enhanced contrast')
    #
    # # print a,b
    # print("a = {}, b = {}\n".format(a, b))
    #
    # # display mapping
    # showMapping(range,a,b)  # add parameters

    # print("b ------------------------------------\n")
    # enhanced2_img, a, b = contrastEnhance(path_image, range)  # add parameters
    # # print a,b
    # print("enhancing an already enhanced image\n")
    # print("a = {}, b = {}\n".format(a, b))

    # print("c ------------------------------------\n")
    # mdist = minkowski2Dist(darkimg_gray,darkimg_gray2)  # add parameters
    # print("Minkowski dist between image and itself\n")
    # print("d = {}\n".format(mdist))
    #
    # print("c ------------------------------------\n")
    #
    # d = meanSqrDist(darkimg_gray,darkimg_gray2)  # add parameters
    # print("mean sqr dist between im1 and im2 = {}\n".format(d))

    # SL = sliceMat(darkimg_gray)

    plt.show()