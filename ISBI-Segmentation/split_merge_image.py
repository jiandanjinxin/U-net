# -*- coding: utf-8 -*-
import time
import shutil
'''
split 30 single images from an array of images : train-volume.tif label-volume.tif test-volume.tif
'''
starttime = time.clock()
from libtiff import TIFF3D, TIFF
import os



dirtype = ("train", "label", "test")


def split_img():
    '''
    split a tif volume into single tif
    '''

    for t in dirtype:
        if os.path.isdir(t):
            shutil.rmtree(t)
            os.mkdir(t)
        else:
            os.mkdir(t)
        imgdir = TIFF3D.open(t + "-volume.tif")
        imgarr = imgdir.read_image()
        for i in range(imgarr.shape[0]):
            imgname = t + "/" + str(i) + ".tif"
            img = TIFF.open(imgname, 'w')
            img.write_image(imgarr[i])


def merge_img():
    '''
    merge single tif into a tif volume
    '''


    path = '/home/greg/data/code/python3/UNet/unet/data/'
    imgdir = TIFF3D.open("test_mask_volume_server2.tif", 'w')
    imgarr = []
    for i in range(30):
        img = TIFF.open(path + str(i) + ".tif")
        imgarr.append(img.read_image())
    imgdir.write_image(imgarr)


if __name__ == "__main__":
    split_img()
    #merge_img()

endtime = time.clock()
print("The split_image running time is %g s" %(endtime-starttime))


