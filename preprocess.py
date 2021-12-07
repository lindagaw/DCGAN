import os
import shutil
dataroot = "..//..//images//Office-31//"

for domain in os.listdir(dataroot):
    for image_type in os.listdir(dataroot + domain + '//images//'):
        src = dataroot + domain + '//images//' + image_type
        dst = dataroot + domain + '//images//' + image_type + '//actual_images//'
        try:
            os.makedirs(dst)
        except Exception as e:
            print(e)
        #os.rename(src, dst)
        for item in os.listdir(src):
            if os.path.isdir(item):
                continue

            original_path = src + '//' + item
            new_path = dst + item
            shutil.move(original_path, new_path)
            print(new_path)
