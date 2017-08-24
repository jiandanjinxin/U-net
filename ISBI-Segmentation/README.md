The following step 
1 split_merge you should install libtiff
  pip install libtiff
  python split_merge_image.py
2 data augmentation the data and label should be the same change
  python augdata.py
3 create newfold for new training data and new label
  sh newtrainnewlabel.sh

4 you should generate npy data
  python generatenpy.py
5 train your unet
  python unet.py
6 test your unet , send the test image into unet

