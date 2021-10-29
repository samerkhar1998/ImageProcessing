import os.path


from hw1_functions import *

if __name__ == "__main__":
    # feel free to add/remove/edit lines


    # path_image = r'Images\darkimage.tif'
    # darkimg = cv2.imread(path_image)
    # darkimg_gray = cv2.cvtColor(darkimg, cv2.COLOR_BGR2GRAY)
    #
    # path_image2 = r'Images\barbara.tif'
    # barbara = cv2.imread(path_image2)
    # barbara_gray = cv2.cvtColor(barbara, cv2.COLOR_BGR2GRAY)

    Images = dict()
    Images_gray = dict()
    folder = os.path.dirname(r'Images\*.tif')
    for img in os.listdir(folder):
        imgName = img.title().split(".", 1)
        readImg = cv2.imread(os.path.join(folder, img))
        Images[imgName[0]] = readImg

        readGrayImg = cv2.cvtColor(readImg, cv2.COLOR_BGR2GRAY)

        Images_gray[imgName[0] + '_gray'] = readGrayImg




    print("Start running script  ------------------------------------\n")
    print_IDs()

    # print("a ------------------------------------\n")
    # Range = [100, 150]
    # enhanced_img, a, b = contrastEnhance(Images_gray['Darkimage_gray'],Range)  # add parameters
    #
    # # display images
    # plt.figure()
    # plt.subplot(1, 2, 1)
    # plt.imshow(Images['Darkimage'])
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
    # showMapping(Range,a,b)  # add parameters
    #
    # print("b ------------------------------------\n")
    # enhanced2_img, a, b = contrastEnhance(enhanced_img,[0,255])  # add parameters
    # # enhanced2_img = cv2.cv2.cvtColor(enhanced2_img,cv2.cv2.COLOR_BGR2GRAY)
    # # print a,b
    # print("enhancing an already enhanced image\n")
    # print("a = {}, b = {}\n".format(a, b))
    #
    # # TODO: display the difference between the two image (Do not simply display both images): Done!
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
    #
    # print("c ------------------------------------\n")
    # mdist = minkowski2Dist(Images_gray['Darkimage_gray'],Images_gray['Darkimage_gray'])  # add parameters
    # print("Minkowski dist between image and itself\n")
    # print("d = {}\n".format(mdist))
    #
    # # TODO: Done
    # # implement the loop that calculates minkowski distance as function of increasing contrast
    # max = np.amax(Images_gray['Darkimage_gray'])
    # min = np.amin(Images_gray['Darkimage_gray'])
    # step = (max - min)/20
    # contrast = []
    # dists = []
    # for i in range(1, 21):
    #     newIm, _, _a = contrastEnhance(Images_gray['Darkimage_gray'], [min, min + i * step])
    #     contrast.append(i*step)
    #     dists.append(minkowski2Dist(Images_gray['Darkimage_gray'], newIm))
    #
    #
    # plt.figure()
    # plt.plot(contrast, dists)
    # plt.xlabel("contrast")
    # plt.ylabel("distance")
    # plt.title("Minkowski distance as function of contrast")
    #
    # print("d ------------------------------------\n")
    # im = Images_gray['Darkimage_gray']
    # tm = np.arange(256)
    # d = np.array(im == np.matmul(sliceMat(im), tm).reshape(len(im), len(im[0]))) # computationally prove that sliceMat(im) * [0:255] == im
    #
    # print("{}".format(d.all()))
    #
    # print("e ------------------------------------\n")
    #
    # nim = contrastEnhance(Images_gray['Darkimage_gray'], [0, 255])
    # TMim, TM = SLTmap(Images_gray['Darkimage_gray'], nim[0])
    # d = np.sum(nim[0] - np.matmul(sliceMat(Images_gray['Darkimage_gray']), TM.transpose()).reshape(len(nim[0]), len(nim[0][0]))) # computationally compare
    # print("sum of diff between image and slices*[0..255] = {}".format(d))
    #
    # # then display
    # plt.figure()
    # plt.subplot(1, 2, 1)
    # plt.imshow(Images['Darkimage'])
    # plt.title("original image")
    # plt.subplot(1, 2, 2)
    # plt.imshow(TMim, cmap='gray', vmin=0, vmax=255)
    # plt.title("tone mapped")
    #
    # print("f ------------------------------------\n")
    # negative_im = sltNegative(Images_gray['Darkimage_gray'])
    # plt.figure()
    # plt.imshow(negative_im, cmap='gray', vmin=0, vmax=255)
    # plt.title("negative image using SLT")
    #
    # print("g ------------------------------------\n")
    # thresh = 120  # play with it to see changes
    # lena = cv2.imread(r"Images\\RealLena.tif")
    # lena_gray = cv2.cvtColor(lena, cv2.COLOR_BGR2GRAY)
    # thresh_im = sltThreshold(lena_gray, thresh)  # add parameters
    #
    # plt.figure()
    # plt.imshow(thresh_im, cmap='gray', vmin=0, vmax=255)
    # plt.title("thresh image using SLT")
    #
    # print("h ------------------------------------\n")
    im1 = Images_gray['Lena_gray']
    im2 = Images_gray['Darkimage_gray']
    SLTim, _ = SLTmap(im1, im2) #TODO : DONE
    #
    # # then print
    # plt.figure()
    # plt.subplot(1, 3, 1)
    # plt.imshow(im1, cmap='gray')
    # plt.title("original image")
    # plt.subplot(1, 3, 2)
    # plt.imshow(SLTim, cmap='gray')
    # plt.title("tone mapped")
    # plt.subplot(1, 3, 3)
    # plt.imshow(im2, cmap='gray', vmin=0, vmax=255)
    # plt.title("tone mapped")
    #
    # d1 = meanSqrDist(im1, im2)# mean sqr dist between im1 and im2
    # d2 = meanSqrDist(SLTim, im2)# mean sqr dist between mapped image and im2
    # print("mean sqr dist between im1 and im2 = {}\n".format(d1))
    # print("mean sqr dist between mapped image and im2 = {}\n".format(d2))

    # print("i ------------------------------------\n")
    # # prove comutationally
    #
    # sl2, _ = SLTmap(im2, im1)
    # d = SLTim == sl2 # TODO: DONE!!!!
    # print(" {}".format(d.all()))

    plt.show()