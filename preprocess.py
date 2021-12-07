import os

dataroot = "..//..//images//Office-31//"

for domain in os.listdir(dataroot):
    for image_type in os.listdir(dataroot + domain):
        src = dataroot + domain + '\\' + image_type
        dst = dataroot + domain+ '\\' + image_type + '\\actual_images\\'
        os.rename(src, dst)
