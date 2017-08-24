# #批量重命名
for var in ./train/*.tif;do mv "$var" "${var%.tif}_train.tif";done
for var in ./label/*.tif;do mv "$var" "${var%.tif}_label.tif";done

#mkdir newfold
if [ -d "newtrain" ]; then
	rm -rf newtrain
	mkdir newtrain 
else
	mkdir newtrain
fi

if [ -d "newlabel" ]; then
	rm -rf newlabel
	mkdir newlabel
else
	mkdir newlabel
fi

# #linux 复制多个文件夹下的文件到一个文件夹下面
for i in $(find ./aug_label/ -name \*.tif); do cp -rf $i ./newlabel/; done
for i in $(find ./aug_train/ -name \*.tif); do cp -rf $i ./newtrain/; done
for i in $(find ./train/ -name \*.tif); do cp -rf $i ./newtrain/; done
for i in $(find ./label/ -name \*.tif); do cp -rf $i ./newlabel/; done