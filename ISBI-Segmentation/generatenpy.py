# -*- coding: utf-8 -*-
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
import numpy as np
import os
import glob
import cv2
import matplotlib.pyplot as plt
#from libtiff import TIFF
import time

starttime = time.clock()




class dataProcess(object):
    def __init__(self, out_rows, out_cols, data_path="newtrain", label_path="newlabel",
                 test_path="test", npy_path="npydata", img_type="tif"):

        """

        """

        self.out_rows = out_rows
        self.out_cols = out_cols
        self.data_path = data_path
        self.label_path = label_path
        self.img_type = img_type
        self.test_path = test_path
        self.npy_path = npy_path

    def create_train_data(self):
        # 将训练集和label分别生成npy格式, 训练集是分离之后的图像
        i = 0
        print('-' * 30)
        print('Creating training images...')
        print('-' * 30)
        imgs = glob.glob(self.data_path + "/*." + self.img_type)           # deform/train
        print(len(imgs))
        imgdatas = np.ndarray((len(imgs), self.out_rows, self.out_cols, 1), dtype=np.uint8)
        imglabels = np.ndarray((len(imgs), self.out_rows, self.out_cols, 1), dtype=np.uint8)
        for imgname in imgs:
            midname = imgname[imgname.rindex("/") + 1:]   # 图像的名字
            img = load_img(self.data_path + "/" + midname, grayscale=True)   # 转换为灰度图
            label = load_img(self.label_path + "/" + midname[:-9] + 'label' + midname[-4:], grayscale=True)
            img = img_to_array(img)
            label = img_to_array(label)
            imgdatas[i] = img
            imglabels[i] = label
            if i % 100 == 0:
                print('Done: {0}/{1} images'.format(i, len(imgs)))
            i += 1
        print('loading done', imgdatas.shape)
        np.save(self.npy_path + '/imgs_train.npy', imgdatas)            # 将30张训练集和30张label生成npy数据
        np.save(self.npy_path + '/imgs_mask_train.npy', imglabels)
        print('Saving to .npy files done.')





    
    

    def create_test_data(self):

        # 将训练集和label分别生成npy格式, 训练集是分离之后的图像
        i = 0
        print('-' * 30)
        print('Creating training images...')
        print('-' * 30)
        imgs = glob.glob(self.test_path + "/*." + self.img_type)           # deform/train
        print(len(imgs))
        imgdatas = np.ndarray((len(imgs), self.out_rows, self.out_cols, 1), dtype=np.uint8)
        for imgname in imgs:
            midname = imgname[imgname.rindex("/") + 1:]   # 图像的名字
            img = load_img(self.test_path + "/" + midname, grayscale=True)   # 转换为灰度图
            img = img_to_array(img)
            imgdatas[i] = img
            if i % 100 == 0:
                print('Done: {0}/{1} images'.format(i, len(imgs)))
            i += 1
        print('loading done', imgdatas.shape)
        np.save(self.npy_path + '/imgs_test.npy', imgdatas)            # 将30张训练集和30张label生成npy数据
        # np.save(self.npy_path + '/imgs_mask_train.npy', imglabels)
        print('Saving to .npy files done.')

    def load_train_data(self):
        # 读入训练数据包括label_mask(npy格式), 归一化(减去了均值,除以方差)
        print('-' * 30)
        print('load train images...')
        print('-' * 30)
        imgs_train = np.load(self.npy_path + "/imgs_train.npy")
        imgs_mask_train = np.load(self.npy_path + "/imgs_mask_train.npy")
        imgs_train = imgs_train.astype('float32')
        imgs_mask_train = imgs_mask_train.astype('float32')
        imgs_train /= 255
        #mean = imgs_train.mean(axis=0)
        #imgs_train -= mean
        
        mean = np.mean(imgs_train)  # mean for data centering
        std = np.std(imgs_train)  # std for data normalization

        imgs_train -= mean
        imgs_train /= std
        
        
        
        imgs_mask_train /= 255
        imgs_mask_train[imgs_mask_train > 0.5] = 1
        imgs_mask_train[imgs_mask_train <= 0.5] = 0
        return imgs_train, imgs_mask_train

    def load_test_data(self):
        print('-' * 30)
        
        print('load train images...')
        print('-' * 30)
        imgs_train = np.load(self.npy_path + "/imgs_train.npy")
        imgs_train = imgs_train.astype('float32')
        imgs_train /= 255
        mean = imgs_train.mean(axis=0)
        mean = np.mean(imgs_train)  # mean for data centering
        std = np.std(imgs_train)  # std for data normalization
        
        
        print('load test images...')
        print('-' * 30)
        imgs_test = np.load(self.npy_path + "/imgs_test.npy")
        imgs_test = imgs_test.astype('float32')
        imgs_test /= 255
        #mean = imgs_test.mean(axis=0)
        imgs_test -= mean
        imgs_test /= std
        return imgs_test


if __name__ == "__main__":

    mydata = dataProcess(512, 512)
    mydata.create_train_data()
    mydata.create_test_data()
    imgs_train, imgs_mask_train = mydata.load_train_data()
    print(imgs_train.shape, imgs_mask_train.shape)

endtime = time.clock()
print("The generatenpy running time is %g s" %(endtime-starttime))
