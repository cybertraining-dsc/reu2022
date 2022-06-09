# Ramdisk

---

![](images/learning.png) **Learning Objectives**

* Learn how to set up a RAM disk
* Learn how to use a DAM disk

---

how to set up aand manage a ramdisk on lunux

develop cms program 


cms ramdisk --... --size=SIZE

use humanize so we can us 1GB for size ...

showcase 

a) dynamic ramdisk no reboot needed, but if reboot, ramdisk needs to
be set up new

b) ramdisk integrated in fstab with reboot

c) backu and load ramdisk


On macOS a RAM disk with 512MB space can be created with the following
command:

```
n = 512 * 2048
os.system('diskutil eraseVolume HFS+ "RAMDisk" `hdiutil attach -nomount ram://{n}`')
```

## Ubuntu

On Ubuntu, a RAM disk and its read-only shadow can be created by:

```
mount -t tmpfs -o size=512m tmpfs /mnt/ramdisk
mount -t aufs -o br:/mnt/ramdisk=ro none /mnt/readonly
```

```
# mkdir /tmp/ramdisk; chmod 777 /tmp/ramdisk
# mount -t tmpfs -o size=256M tmpfs /tmp/ramdisk/
```

using /dev/shm: 

http://ubuntuguide.net/ubuntu-using-ramdisk-for-better-performance-and-fast-response

Various methods:
(in german): https://wiki.ubuntuusers.de/RAM-Disk_erstellen/

ramfs is an older file system type and is replaced in mostly by tmpfs.

## windows

https://forums.guru3d.com/threads/guide-using-imdisk-to-set-up-ram-disk-s-in-windows-with-no-limit-on-disk-size.356046/
