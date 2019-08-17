Title: darktable and opencl in Ubuntu 19.04
Started: 2019-08-17 12:43:26
Date: 2019-08-17 12:43:26
Slug: darktable-opencl-ubuntu1904
Location: Vacation house 201901
Authors: Michiel Scholten
Category: howto
Tags: desktop, howto, linux, photography, tech
Status: published

Editing and even viewing (raw) photographs can be a bit taxing on your CPU. If you have an Nvidia GPU, you can supercharge your photo editor by using its OpenCL extensions to offload operations to. Using [darktable](https://www.darktable.org/) myself, I had to do a minor bit of research before it worked, as package names have changed in recent Ubuntu.

Assuming you already have nvidia-driver-390 and nvidia-prime installed and switched to use nvidia using `prime-select nvidia` (when relevant if you switch between using the built-in Intel GPU and your Nvidia chip for example), there's some packages that need installing before OpenCL works with darktable:

    sudo apt install nvidia-headless-390 nvidia-modprobe opencl-headers ocl-icd-libopencl1

Now reboot (or restart X), start darktable and check its settings (little cog icon, 'preferences'). In the 'core options' tab you will now see a checkbox next to 'activate OpenCL support'. Enable and engage :)
