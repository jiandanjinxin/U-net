The following step 

(1) split_merge you should install libtiff
  ```
  pip install libtiff
  python split_merge_image.py
  ```
  
(2)data augmentation the data and label should be the same change
  ```
  python augdata.py
  ```
  
(3)create newfold for new training data and new label
  ```
  sh newtrainnewlabel.sh
  ```

(4)you should generate npy data
  ```
  python generatenpy.py
  ```
  
(5)train your unet
  ```
  python unet.py
  ```
  
(6)test your unet , send the test image into unet

**Reference**

[zhixuhao/unet](https://github.com/zhixuhao/unet)

[全卷机神经网络图像分割(U-net)-keras实现](http://blog.csdn.net/u012931582/article/details/70215756) 

[silencemao/detect-cell-edge-use-unet](https://github.com/silencemao/detect-cell-edge-use-unet)

[U-net使用, 图像分割(边缘检测)](http://blog.csdn.net/qq_18293213/article/details/72423592)
