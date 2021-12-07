import os

dataroot = "..//..//images//Office-31//"

for domain in os.listdir(dataroot):
    for image_type in os.listdir(os.join(dataroot, domain)):
        src = os.join(dataroot, domain, directory)
        dst = os.join(dataroot, domain, directory, images)
        os.rename(src, dst)
