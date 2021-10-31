import os.path


from hw1_functions import *

if __name__ == "__main__":

    Images = dict()
    Images_gray = dict()
    folder = os.path.dirname(r'Images\*.tif')
    for img in os.listdir(folder):
        imgName = img.title().split(".", 1)
        readImg = cv2.imread(os.path.join(folder, img))
        Images[imgName[0]] = readImg

        readGrayImg = cv2.cvtColor(readImg, cv2.COLOR_BGR2GRAY)

        Images_gray[imgName[0] + '_gray'] = readGrayImg
    # Images_gray keys are : Barbara_gray', 'Barbarasmall_gray', 'Binary1_gray', 'Binary2_gray', 'Binary3_gray', 'Cups_gray',
    # 'Darkimage_gray', 'Flathistogram_gray', 'Foursquares_gray', 'Fruit_gray', 'Gausshistogram_gray', 'Lakescene_gray',
    # 'Lena_gray', 'Lenabw_gray', 'Lighthouse_gray', 'Mountainscene_gray', 'Racecar_gray', 'Random_gray', 'Reallena_gray',
    # 'Ricefields_gray', 'Square_gray', 'Stroller_gray', 'Tools_gray', 'Wine_gray'])


    # Images keys are: Barbara', 'Barbarasmall', 'Binary1', 'Binary2', 'Binary3', 'Cups', 'Darkimage', 'Flathistogram',
    # 'Foursquares', 'Fruit', 'Gausshistogram', 'Lakescene', 'Lena', 'Lenabw', 'Lighthouse', 'Mountainscene', 'Racecar',
    # 'Random', 'Reallena', 'Ricefields', 'Square', 'Stroller', 'Tools', 'Wine'])


    # print("Start running script  ------------------------------------\n")
    # print_IDs()
    #
    # print("a ------------------------------------\n")
    # Range = [100, 150]
    # enhanced_img, a, b = contrastEnhance(Images_gray['Lena_gray'],Range)  # add parameters
    #
    # # display images
    # plt.figure()
    # plt.subplot(1, 2, 1)
    # plt.imshow(Images['Lena'])
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
    # showMapping(Range, a, b)  # add parameters
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
    # negative_im = sltNegative(Images_gray['Binary1_gray'])
    # plt.figure()
    # plt.imshow(negative_im, cmap='gray', vmin=0, vmax=255)
    # plt.title("negative image using SLT")

    # print("g ------------------------------------\n")
    # thresh = 120  # play with it to see changes
    # thresh_im = sltThreshold(Images_gray['Reallena_gray'], thresh)  # add parameters
    #
    # plt.figure()
    # plt.imshow(thresh_im, cmap='gray', vmin=0, vmax=255)
    # plt.title("thresh image using SLT")

    # print("h ------------------------------------\n")
    # TODO: DONE
    # im1 = Images_gray['Lena_gray']
    # im2 = Images_gray['Reallena_gray']
    # SLTim, _ = SLTmap(im1, im2)
  
    #
    # # then print
    # plt.figure()
    # plt.subplot(1, 3, 1)
    # plt.imshow(im1, cmap='gray')
    # plt.title("original image")
    # plt.subplot(1, 3, 2)
    # plt.imshow(im2, cmap='gray')
    # plt.title("Mapped to")
    # plt.subplot(1, 3, 3)
    # plt.imshow(SLTim, cmap='gray', vmin=0, vmax=255)
    # plt.title("Result of Mapped img1 to im2")

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