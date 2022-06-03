# Ramdisk

how to set up aand manage a ramdisk on lunux

develop cms program 


cms ramdisk --... --size=SIZE

use humanize so we can us 1GB for size ...

showcase 
a) dynamic ramdisk no reboot needed, but if reboot, ramdisk needs to be set up new
b) ramdisk integrated in fstab with reboot
c) backu and load ramdisk


On macOS a RAM disk with 512MB space can be created with the following command:

n = 512 * 2048
os.system('diskutil eraseVolume HFS+ "RAMDisk" `hdiutil attach -nomount ram://{n}`')

On Ubuntu, a RAM disk and its read-only shadow can be created by:

mount -t tmpfs -o size=512m tmpfs /mnt/ramdisk
mount -t aufs -o br:/mnt/ramdisk=ro none /mnt/readonly
